import socket

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

# Connect to server
client.connect((host, port))

while True:
    # Send message to server
    msg = input("Client: ")
    client.send(msg.encode())

    if msg.lower() == "exit":
        break

    # Receive reply from server
    server_msg = client.recv(1024).decode()
    print("Server:", server_msg)

    if server_msg.lower() == "exit":
        break

client.close()