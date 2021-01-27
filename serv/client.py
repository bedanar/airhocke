
import socket

sock = socket.socket()

sock.connect(('localhost', 9090))
while True:
    str = input()
    if len(str) == 0:
        continue
    if str == 'exit':
        break
    str = str.encode('utf-8')
    sock.send(str)
    data = sock.recv(1024)
    print(data)



sock.close()

# print(data)
