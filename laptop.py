import socket
from datetime import datetime


# Set the IP address and port number
#IP_ADDRESS = "172.16.0.160"
IP_ADDRESS = "192.168.1.5"
PORT = 1060
SIZE = 1024
FORMAT = "utf-8"
FORMAT = "utf-8"

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
sock.bind((IP_ADDRESS, PORT))

# Listen for incoming connections
sock.listen(1)
print('Starting The Server at: ', datetime.now())
print("Waiting for a connection...")

# Accept incoming connections
client, addr = sock.accept()
print(f"Connected by {addr}")


# Receive sensor data and datetime over TCP/IP socket communication from RaspBerry Pi Zero W using Python (5)

while True:
   

    filename = client.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the filename.")

    file = open(filename, "w")
    client.send("Filename received.".encode(FORMAT))

    data = client.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    client.send("File data received".encode(FORMAT))

    file.close()

    client.close()
    print(f"[DISCONNECTED] {addr} disconnected.")
    break

sock.close()

 #---------------------------------------------------------