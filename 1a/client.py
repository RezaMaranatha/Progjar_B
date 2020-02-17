import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
host_ip = input("Input Server Ip: ")
port_num = int(input("Input Server Port Number: "))
# host_name = socket.gethostname() 
# host_ip = socket.gethostbyname(host_name)

server_address = (host_ip, port_num)
print("Connecting to Server: ", host_ip , " Port: ", port_num)
sock.connect(server_address)

try:
    # Send data
    message = 'JARINGAN TEKNIK INFORPEMROGRAMAN MATIKA'
    print("Sending: " ,message)
    sock.send(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(1024).decode()
        amount_received += len(data)
        print("Received: " ,data)
finally:
    print("Closing Connection")
    sock.close()
