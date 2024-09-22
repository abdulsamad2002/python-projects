import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host  = "127.0.0.1"
port  = 2002

serversocket.bind((host, port))
serversocket.listen(3)

while(True):
    clientsocket , address = serversocket.accept()
    print("Connection established with {}".format(str(address)))
    message = "Thank you for connecting!"
    clientsocket.send(message.encode("ascii"))
    clientsocket.close()