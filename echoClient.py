import socket

def echo_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Replace with server IP and port
    message = "Hello, this is a test message."
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    client_socket.close()

echo_client()
