import socket
import time

TARGET_IP = "10.151.254.92"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    sock.sendto(bytes('Informatika'.encode()),(TARGET_IP,TARGET_PORT))

