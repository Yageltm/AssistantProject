from tcp_client import TcpClient
from tcp_server import TcpServer
from udp_server import UdpServer
from udp_server import UdpServer
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
        coordinates = helped_udp.listen().split(',')
        print(coordinates)
        # pyautogui.moveTo(int(coordinates[0]), int(coordinates[1]))
        if keyboard.is_pressed('b'):
            break

def get_voice():
    audio = pyaudio.PyAudio()
    voice_format = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024
    voice_getting = UdpServer(9990)
    stream = audio.open(format=voice_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk)

    # Continuously receive audio data from the client and play it
    print('press d to hang up.')
    while True:
        data = voice_getting.listen()
        stream.write(data)
        if keyboard.is_pressed('d'):
            break

