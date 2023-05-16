import socket


class TcpClient:
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_ip = ip
        self.port = port
        self.sock.connect((self.host_ip, self.port))

    def send(self, message):
        self.sock.sendall(message.encode())

    def receive(self):
        data = self.sock.recv(1024).decode()
        print(data)

    def close(self):
        self.sock.close()
