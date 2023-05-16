from tcp_client import TcpClient
from tcp_server import TcpServer
from udp_server import UdpServer
from udp_server import UdpServer
import pyautogui
import keyboard
import socket

# invite assistant to help in those ports
invite = TcpClient('10.100.102.29', 8000)
invite.send(f'help:{socket.gethostbyname(socket.gethostname())}:{3456}:{12345}')
invite.receive()
invite.close()

# first connection to assistants
helped_tcp = TcpServer(3456)
print(f'assistant: {helped_tcp.listen()}')
helped_udp = UdpServer(12345)
print(f'assistant: {helped_udp.listen()}')


def mouse_mover():
    print('push b to stop assistant control')
    while True:
        coordinates = helped_udp.listen().split(',')
        print(coordinates)
        # pyautogui.moveTo(int(coordinates[0]), int(coordinates[1]))
        if keyboard.is_pressed('b'):
            break


mouse_mover()
