from socket import *
import os

buffer_size = 4096
line_end = "\r\n"

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.listen(1)
server_port = server_socket.getsockname()[1]


status_code = {
    "200": "OK",
    "201": "Created",
    "400": "Bad Reqeust",
    "404": "Not Found",
    "500": "Internal Server Error",
}


print(f"server is running on port number : {server_port}")


def read_file(file_path) -> bytes:
    """
    Read files in bytes to send over the network.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        bytes: Bytes of the read file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, "rb") as file:
        return file.read()


def parse_request(request: str) -> dict:
    """
    Parse an HTTP request string into a structured dictionary.

    Args:
        request: The raw HTTP request string

    Returns:
        A dictionary containing the parsed request with request line, headers, and body
    """
    request = request.split(line_end)
    request_line = request[0].split(" ")
    if len(request_line) != 3:
        raise ValueError("Invalid request line")

    parsed_request = {
        "request_line": {"method": "-1", "resource": "-1", "version": "-1"},
        "headers": {},
        "body": "",
    }

    parsed_request["request_line"]["method"] = request_line[0]
    parsed_request["request_line"]["resource"] = request_line[1]
    parsed_request["request_line"]["version"] = request_line[2]

    empty_line = False
    for line in range(1, len(request)):
        if request[line] == "":
            empty_line = True
        elif empty_line == False:
            index = request[line].find(":")
            key = request[line][:index]
            value = request[line][index + 1 :]
            parsed_request["headers"][key] = value
        else:
            parsed_request["body"] += request[line] + line_end
    return parsed_request


def create_response(request: dict) -> bytes:
    method = parsed_request["request_line"]["method"]
    resource = parsed_request["request_line"]["resource"]
    if not resource.startswith("."):
        resource = "." + resource
    if method in {"GET", "HEAD"}:

        if os.path.isdir(resource):
            resource += "/index.html"

        if os.path.isfile(resource):
            status_line = (f"HTTP/1.1 200 {status_code["200"]}" + line_end).encode()
            headers = "".encode()
            body = read_file(resource)
            response = status_line + headers + line_end.encode()

            if parsed_request["request_line"]["method"] == "GET":
                response += body

            return response
        else:
            status_line = f"HTTP/1.1 404 {status_code['404']}" + line_end
            return status_line.encode()
    elif method == "PUT":
        content = parsed_request["body"]
        dir = os.path.splitext(resource)[0]
        if os.path.isdir(dir):
            if dir == resource:
                return (f"HTTP/1.1 400 {status_code["400"]}{line_end}").encode()
            update = os.path.isfile(resource)
            code = 204 if update else 201
            with open(resource, "w") as file:
                file.write(content)
            response = (
                f"HTTP/1.1 {code} {status_code[str(code)]}{line_end}"
                f"Connection: close{line_end}"
                f"{line_end}"
            )
            return response.encode()
        else:
            status_line = f"HTTP/1.1 404 {status_code['404']}" + line_end
            return status_line.encode()
    else:
        response = f"HTTP/1.1 500 {status_code['500']}" + line_end
        return response.encode()


try:
    while True:
        print(f"server is ready to listen for request")
        connectionSocket, addr = server_socket.accept()
        request = connectionSocket.recv(buffer_size).decode()
        parsed_request = parse_request(request)
        print(parsed_request["request_line"])
        print(create_response(parsed_request).decode())
        connectionSocket.send(create_response(parsed_request))
        connectionSocket.close()
except KeyboardInterrupt:
    print(f"server has been closed :)")
finally:
    print(f"Al salam Alaykom :)")

server_socket.close()
