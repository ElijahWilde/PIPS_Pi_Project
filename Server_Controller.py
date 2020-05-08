import numpy as np
import socket
import pickle
import sys

x = 5
firstTime = True
output = []

K = -2

def controller(x):
    u = (K * x)
    #u = 0
    return u

hostMACAddress = 'DC:A6:32:60:0E:46'
port = 3
backlog = 1
size = 1024

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)

client, address = s.accept()

try:
    while True:
       
        if firstTime:
            x = x
        else:
            x = client.recv(size)
            x = float((x).decode('utf-8')) #x = pickle.loads(x)
       
        if x: #type(x) == int or len(x)> 0
            u = controller(x)
            output.append(x)
           
            print(type(x))
            print('x:',x)
            print(type(u))
            print('u:',u)
           
            u = str(u).encode('utf-8') #u = pickle.dumps(u)
            firstTime = False
            client.send(u) #client.send(u,'UTF-8')

except:
    e = sys.exc_info()[0]
    print(e)
    print("Closing Socket")
    client.close()
    s.close()
   

import matplotlib.pyplot as plt  
   
myRange = range(0, len(output))    
plt.plot(myRange, output)  
   

plt.savefig('graph.png')
plt.show()

    
