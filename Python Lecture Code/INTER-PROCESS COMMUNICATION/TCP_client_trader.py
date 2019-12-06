import socket
import sys

HOST, PORT = "localhost", 9999
data = "seb"

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    print('here')
    print("Sent:     {}".format(data))
    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
    print("Received: {}".format(received))
