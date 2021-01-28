#!/usr/bin/env python3

## UDP client/server

import socket
import sys
import threading

def receive(s):
    while True:
        r = s.recvfrom(1024)

        data = r[0]
        addr = r[1]

        if not data:
            break

        print("[" + addr[0] + ":" + str(addr[1]) + "]" + " : " + data.decode().strip())

def send(s):
    while True:
        msg = input("Enter a message to send to Host: ").encode()
        
        try:
            s.sendto(msg, (CLIENT, PORT))
        except socket.error as errmsg:
            print("Failed to send message. Error: \"" + str(errmsg) + "\"")

HOST = ""
CLIENT = input("Enter CLIENT IP address: ")

PORT = 2789

# Init socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created!")
except socket.error as errmsg:
    print("Failed to create socket \" " + str(errmsg) + "\"")
    sys.exit()

# Bind to HOST, PORT
try: 
    s.bind((HOST, PORT))
    print("Bind succesful!")
except socket.error as errmsg:
    print("Failed to bind to host \"" + HOST + "\" and port \"" + str(PORT) + "\": \"" + str(errmsg) + "\"")
    sys.exit()

receiver = threading.Thread(target=receive, args=(s, ))
sender = threading.Thread(target=send, args=(s, ))

receiver.start()
sender.start()