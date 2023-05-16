import socket


class TcpServer:
    def __init__(self, port):
        self.client_socket = None
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_ip = socket.gethostbyname(socket.gethostname())
        socket_address = (self.host_ip, port)
        self.server_socket.bind(socket_address)

    def listen(self):
        self.server_socket.listen()
        while True:
            self.client_socket, address = self.server_socket.accept()
            data = self.client_socket.recv(1024).decode()
            return data

    def send(self, message):
        if self.client_socket is not None:
            self.client_socket.sendall(message.encode())

    def close(self):
        self.client_socket.close()
        self.server_socket.close()
