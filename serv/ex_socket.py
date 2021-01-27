import socket


class MySocket:
    def __init__(self, sock=None):
        if sock:
            self.sock = sock
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.sock.connect((host, port))

    def my_send(self, msg):
        total_sends = 0
        while total_sends < MSGLIMIT:
            sent = self.sock.send(msg[total_sends:])
            if sent == 0:
                raise RuntimeError("Connection is broken")
            total_sends += sent

    def my_receive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLIMIT:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("Connection is broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)

        return b''.join(chunks)
