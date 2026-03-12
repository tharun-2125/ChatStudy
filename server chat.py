import socket

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

# Bind and listen
server.bind((host, port))
server.listen(1)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    # Receive message from client
    client_msg = conn.recv(1024).decode()
    print("Client:", client_msg)

    if client_msg.lower() == "exit":
        break

    # Send message to client
    msg = input("Server: ")
    conn.send(msg.encode())

    if msg.lower() == "exit":
        break

conn.close()
server.close()