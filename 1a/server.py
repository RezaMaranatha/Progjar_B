import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_num = int(input("Input Port Number: "))
# Bind the socket to the port
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name)
server_address = (host_ip, port_num)
print("Starting Server on ", host_ip, " Port: ", port_num)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    print("Waiting for Connection")
    connection, client_address = sock.accept()
    print("Connection from" ,client_address)
    while True:
        data = connection.recv(1024).decode()
        print("received" , data)
        if data:
            print("sending back data")
            connection.send(data.encode())
        else:
            print("no more data from" ,client_address)
            break
    connection.close()
    print ("client disconnected")
