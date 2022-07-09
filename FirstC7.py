import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(socket.gethostbyname(socket.gethostname()))
s.listen(50)
s.accept()
s.connect(socket.gethostbyname(socket.gethostname()))
print("Connected")
