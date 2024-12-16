#!/usr/bin/python3

import socket

# created a server socket object, specified family and type
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specified host name and port
host = socket.gethostbyname()
port = 444

# assigns the server socket to a specific address
serversocket.bind((host, port))

# listens to connection up to maximum of 3
serversocket.listen(3)

# while all of above is true
while True:
    clientsocket, address = serversocket.accept()

    print("received connection from " % str(address))

    message = 'Thank you for connecting!' + '\r\n'
    clientsocket.send(message)

    clientsocket.close()