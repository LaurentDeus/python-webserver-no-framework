import socket

def handle_request(request):
    # This function handles incoming HTTP requests
    # Here, you could parse the request, generate a response, etc.
    return b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"

def main():
    # Define host and port
    host = '127.0.0.1'
    port = 8080

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive data from client
        request = client_socket.recv(1024)

        # Handle the request and generate a response
        response = handle_request(request)

        # Send response back to client
        client_socket.sendall(response)

        # Close the connection with the client
        client_socket.close()

if __name__ == "__main__":
    main()
