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
    print ("Requesting File to Server")
    sock.send(file_name.encode())
    while True:
        data = sock.recv(1024)
        temp = open("res_"+file_name,"a+b")
        if not data:
            temp.close()
            break
        temp.write(data)
    print("File has been Received")
finally:
    print("Closing Connection")
    sock.close()
