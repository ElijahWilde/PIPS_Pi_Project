# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:16:01 2020

CLIENT
"""

import socket
import numpy as np
import pickle
import os

#SETUP CLIENT
numCycles = 1000
A = 1.5 #dynamics "matrix"
B = 1 #input "matrix"
size = 1024
oldX = 5

def model(u, oldX):
    x = (A * oldX) + (B * u)
    return x

serverMACAddress ='DC:A6:32:60:0E:46'
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

while True:
    numCycles -= 1
    print("Cycle:",numCycles)
    if numCycles <= 0:
        break
   
    u = s.recv(size)

    if (len(u) > 0):
        u = float((u).decode('utf-8'))#u = pickle.loads(u)
        x = model(u, oldX)
        oldX = x
       
        x = str(x).encode('utf-8')#x = pickle.dumps(x)
        s.send(x)
       
print("Closing Connection...")
s.close()

