import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
host_ip = input("Input Server Ip Address: ")
port_num = int(input("Input Server Port Number: "))
# host_name = socket.gethostname() 
# host_ip = socket.gethostbyname(host_name)

server_address = (host_ip, port_num)
print("Connecting to Server: ", host_ip , " Port: ", port_num)
sock.connect(server_address)

try:
    # Send data
    file_name="test.txt"
    temp = open(file_name,"rb")
    file = temp.read()
    print ('Sending data to Server')
    sock.send(file)
finally:
    print("Closing Connection")
    sock.close()
