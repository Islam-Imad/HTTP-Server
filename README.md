# HTTP-Server

This project is a lightweight HTTP server implemented in Python. It is designed to handle basic HTTP requests such as `GET`, `HEAD`, and `PUT`. The server is built using Python's `socket` module and provides a simple way to serve files and handle HTTP requests.

## Features

- **GET and HEAD Requests**: 
  - Serves static files from the server's directory.
  - Automatically serves `index.html` if a directory is requested.
  - Returns appropriate HTTP status codes (`200 OK`, `404 Not Found`).

- **PUT Requests**:
  - Allows uploading or updating files on the server.
  - Creates new files or updates existing ones.
  - Returns appropriate HTTP status codes (`201 Created`, `204 No Content`, `400 Bad Request`, `404 Not Found`).

- **Error Handling**:
  - Handles invalid requests with proper HTTP status codes (`400 Bad Request`, `500 Internal Server Error`).

- **Customizable**:
  - Easily extendable to support additional HTTP methods or features.

## How It Works

1. The server listens for incoming connections on a dynamically assigned port.
2. When a request is received, it is parsed into a structured dictionary containing the request line, headers, and body.
3. Based on the HTTP method (`GET`, `HEAD`, or `PUT`), the server generates an appropriate response.
4. The response is sent back to the client, and the connection is closed.

## Usage

1. Clone the repository and navigate to the project directory.
2. Run the server using Python:
   ```bash
   python WebServer.py
   ```
3. The server will display the port number it is running on. For example:
   ```
   server is running on port number : 8080
   ```
4. Use a web browser, `curl`, or any HTTP client to send requests to the server.

### Example Requests

- **GET Request**:
  ```bash
  curl http://localhost:8080/index.html
  ```

- **HEAD Request**:
  ```bash
  curl -I http://localhost:8080/index.html
  ```

- **PUT Request**:
  ```bash
  curl -X PUT -d "Hello, World!" http://localhost:8080/newfile.txt
  ```

## File Structure

- `WebServer.py`: The main Python script implementing the HTTP server.
- `README.md`: Documentation for the project.

## HTTP Status Codes Supported

- `200 OK`: Request succeeded, and the resource is returned.
- `201 Created`: Resource successfully created.
- `204 No Content`: Resource successfully updated.
- `400 Bad Request`: Invalid request format.
- `404 Not Found`: Requested resource not found.
- `500 Internal Server Error`: Server encountered an unexpected condition.

## Limitations

- This server is designed for educational purposes and is not production-ready.
- It does not support HTTPS or advanced HTTP features like authentication, cookies, or sessions.

## Future Improvements

- Add support for additional HTTP methods (e.g., `POST`, `DELETE`).
- Implement HTTPS for secure communication.
- Add logging and better error handling.
- Support for concurrent connections using threading or asynchronous programming.

## License

This project is open-source and available under the MIT License.