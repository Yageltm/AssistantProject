import socket


class UdpServer:
    def __init__(self, port):
        self.client_address = None
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.host_ip = socket.gethostbyname(socket.gethostname())
        server_address = ('127.0.0.1', self.port)
        self.server_socket.bind(server_address)

    def listen(self):
        while True:
            data, self.client_address = self.server_socket.recvfrom(1024)
            return data.decode()

    def send(self, message):
        self.server_socket.sendto(message.encode(), self.client_address)
