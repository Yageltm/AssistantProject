import socket


class UdpClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (self.ip, self.port)
        self.client_socket.connect(server_address)

    def send(self, message):
        self.client_socket.sendall(message.encode())

    def receive(self):
        response = self.client_socket.recv(1024)
        return response
