import socket
import threading

# Choose the protocol
protocol = input("Choose the protocol, type 1 for TCP and 2 for UDP: ")

myp = socket.SOCK_STREAM
if protocol == "2": myp = socket.SOCK_DGRAM

server=socket.socket( socket.AF_INET, myp )
ip= '192.168.0.109'
port = 1234
server.bind((ip,port))

# TCP
if protocol == "1":
    server.listen(1)
    conn, addr = server.accept()
    print("Connection from: " + str(addr))

    while True:
        data = conn.recv(1024).decode('ascii')
        if not data:
            break
        print("Cliente: " + str(data))
        data = input(' -> ')
        conn.send(data.encode('ascii'))

# UDP
elif protocol == "2":
    while True:
        x=server.recvfrom(1024)
        data = x[0].decode()
        print("Cliente: " + data)
        data = input(' -> ')
        server.sendto(data.encode('ascii'),x[1])
else:
    print("Invalid protocol")