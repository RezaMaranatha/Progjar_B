import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)

try:
    filename="tes.txt"
    msg = "get "+filename
    print ("Requesting File to Server")
    sock.send(msg.encode())

    data = sock.recv(4096)
    temp = open(filename,"wb")
    temp.write(data)
    temp.close()
    
    print("File has been Received")
finally:
    print("Closing Connection")
    sock.close()