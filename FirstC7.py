import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.recv(1000)
