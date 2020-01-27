import socket
import sys
import time

s=socket.socket()
host=input(str("Please enter the hostname of the server : "))
port=8080
s.connect((host,port))
print("Connection succesfull")

while 1:
    incoming_msg = s.recv(1024)#1024 bytes per package
    incoming_msg=incoming_msg.decode()
    print("server:",incoming_msg)

    message=input(str(">>"))
    message=message.encode()
    s.send(message)
    print("Msg has been sent..")
