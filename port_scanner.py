import socket
import sys

if len(sys.argv) != 3:
    print("Invalid arguments!")
    print("python3 <scriptname> <target_ip> <target_port>")
    exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
host = str(sys.argv[1])
port = int(sys.argv[2])

def portScanner(port):
    if s.connect_ex((host, port,)):
        print("Port is closed")
    else:
        print("The port is open")

portScanner(port)