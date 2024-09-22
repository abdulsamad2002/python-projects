import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 2002
clientsocket.connect((host, port))

message = clientsocket.recv(2048)

print(message.decode('ascii'))