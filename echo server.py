import socket

# Define server IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")

while True:
    message = input("Enter message to send (Type 'exit' to close connection): ")

    if message.lower() == 'exit':
        break

    # Send data to the server
    client_socket.sendall(message.encode())

    # Receive echoed data from the server
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")

# Close the connection
client_socket.close()
