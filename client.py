import socket
import threading

# Choose the protocol
protocol = input("Choose the protocol, type 1 for TCP and 2 for UDP: ")

myp = socket.SOCK_STREAM
if protocol == "2": myp = socket.SOCK_DGRAM

server=socket.socket( socket.AF_INET, myp )
ip= '192.168.0.109'
port = 1234
server.connect((ip,port))

# TCP
if protocol == "1":

    while True:
        data = input(' -> ')
        server.send(data.encode('ascii'))
        data = server.recv(1024)
        print("Servidor: " + str(data.decode('ascii')))

# UDP
elif protocol == "2":

    while True:
        data=input(' -> ')
        server.sendto(data.encode('ascii'),(ip,port))
        data,addr=server.recvfrom(1024)
        print("Servidor: ",data.decode('ascii'))

else:
    print("Invalid protocol")
