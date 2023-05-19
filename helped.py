from tcp_client import TcpClient
from tcp_server import TcpServer
from udp_server import UdpServer
from udp_server import UdpServer
from voice_server import get_voice
from voice_client import send_voice
import pyautogui
import keyboard
import socket
import pyaudio

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
        message = helped_udp.listen()
        if message == 'right':
            pyautogui.click(button='right')
        elif message == 'left':
            pyautogui.click()
        else:
            coordinates = message.split(',')
            print(coordinates)
            pyautogui.moveTo(int(coordinates[0]), int(coordinates[1]), 0.2)
        if keyboard.is_pressed('b'):
            break


