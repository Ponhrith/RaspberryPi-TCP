#---------------------------------------------------------------------------

#work
# import mysql.connector
# import socket
# from datetime import datetime

# # HOST = socket.gethostbyname(socket.gethostname())
# #HOST = socket.gethostbyname("192.168.1.7")
# HOST = socket.gethostbyname("172.16.0.160")
# #HOST = socket.gethostbyname("172.16.1.68")
# PORT = 1060
# SIZE = 1024
# FORMAT = "utf-8"
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind((HOST, PORT))
# print('Starting The Server at: ', datetime.now())
# print("Waiting to accept a new connection")
# sock.listen(5)
# client, addr = sock.accept()


# # Receive sensor data and datetime over TCP/IP socket communication from RaspBerry Pi Zero W using Python (5)

# while True:
   

#     filename = client.recv(SIZE).decode(FORMAT)
#     print(f"[RECV] Receiving the filename.")

#     file = open(filename, "w")
#     client.send("Filename received.".encode(FORMAT))

#     data = client.recv(SIZE).decode(FORMAT)
#     print(f"[RECV] Receiving the file data.")
#     file.write(data)
#     client.send("File data received".encode(FORMAT))

#     file.close()

#     client.close()
#     print(f"[DISCONNECTED] {addr} disconnected.")
#     break

# sock.close()

# # Store sensor data and datetime in a persistent media (MySQL or local file) (6)

# dataBase = mysql.connector.connect(

#     host="localhost",

#     user="root",

#     passwd="",

#     database="hdsd"
# )


# cursorObject = dataBase.cursor()
# f = open("Report.txt", "r")
# end_of_file = f.readline()
# for x in f:
#     res = x.split()
#     sql = "INSERT INTO STUDENT (NAME, EMAIL) VALUES (%s, %s)"
#     val = (str(res[0]), str(res[1]))
#     cursorObject.execute(sql, val)
#     dataBase.commit()
#     if not end_of_file:
#         break

#-------------------------------------------------------------------------
#work2

# import socket
# #import os
# import time

# # Set the IP address and port number
# IP_ADDRESS = "172.16.0.160"
# PORT = 1060
# SIZE = 1024
# FORMAT = "utf-8"

# # Create a socket object
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to a specific address and port
# sock.bind((IP_ADDRESS, PORT))

# # Listen for incoming connections
# sock.listen(1)

# print("Waiting for a connection...")

# # Accept incoming connections
# conn, addr = sock.accept()

# print(f"Connected by {addr}")

# # Send sensor data and datetime over TCP/IP socket communication to laptop using Python
# filename = "Report.txt"

# while True:
#     # Read the sensor data and datetime
#     data = "Report:"
#     now = time.strftime("%Y-%m-%d %H:%M:%S")

#     # Write the sensor data and datetime to a file
#     with open(filename, "w") as f:
#         f.write(f"{data}\n{now}")

#     # Send the file to the laptop
#     with open(filename, "rb") as f:
#         conn.send(filename.encode(FORMAT))
#         conn.recv(SIZE)


#--------------------------------------------
#work3

# import socket
# import time

# # Set the IP address and port number
# IP_ADDRESS = "172.16.0.160"
# PORT = 1060
# SIZE = 1024
# FORMAT = "utf-8"

# # Create a socket object
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to a specific address and port
# sock.bind((IP_ADDRESS, PORT))

# # Listen for incoming connections
# sock.listen(1)

# print("Waiting for a connection...")

# # Accept incoming connections
# conn, addr = sock.accept()
# print(f"Connected by {addr}")

# # Send sensor data and datetime over TCP/IP socket communication to laptop using Python
# filename = "Report.txt"

# while True:
#     # Read the sensor data and datetime
#     data = "Report:"
#     now = time.strftime("%Y-%m-%d %H:%M:%S")

#     # Write the sensor data and datetime to a file
#     with open(filename, "w") as f:
#         f.write(f"{data}\n{now}")

#     # Send the file to the laptop
#     with open(filename, "rb") as f:
#         conn.send(filename.encode(FORMAT))
#         conn.recv(SIZE)
#         print("File received")
#         conn.close()
#         break

#---------------------------------------------------------


import socket
from datetime import datetime


# Set the IP address and port number
IP_ADDRESS = "172.16.0.160"
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

 