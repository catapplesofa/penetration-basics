#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
host_ip = socket.gethostbyname(host) 
port = 444

clientsocket.connect((host_ip, port))

# max data allowed to come to port
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))