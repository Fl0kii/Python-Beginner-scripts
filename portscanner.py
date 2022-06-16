#!/user/bin/python3

#Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.
import socket

#AF_INET refers to the address-family ipv4
#The SOCK_STREAM means connection-oriented TCP protocol

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = input("Enter IP Address: ")
port = int(input("Enter Port number: "))
s.settimeout(6)
#Without the int conversion, it gives this error code TypeError: 'str' object cannot be interpreted as an integer

#Creating a function to do the actual scanning.
def portscanner(port):
    if s.connect_ex((IP, port)):
        print("Port is closed")
#s.connect_ex returns an error code when unable to connect.
    else:
        print("Port is open")

portscanner(port)
    




