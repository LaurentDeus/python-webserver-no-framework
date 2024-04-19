import socket

# Define the server's host and port
server_host = '127.0.0.1'
server_port = 8080

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Send a message to the server
message = "Hello, server!"
client_socket.sendall(message.encode())

# Receive a response from the server
response = client_socket.recv(1024)
print("Received from server:", response.decode())

# Close the socket
client_socket.close()
