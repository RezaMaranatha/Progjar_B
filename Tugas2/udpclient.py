import socket
import time

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    sock.sendto(bytes('Informatika'.encode()),(TARGET_IP,TARGET_PORT))

