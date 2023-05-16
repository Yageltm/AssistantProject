from tcp_client import TcpClient
from tcp_server import TcpServer
from udp_client import UdpClient
from udp_server import UdpServer
import pyaudio
import pyautogui
import time

# first run to get calls for help
savior = TcpServer(8000)
print('ready to help')
addresses = savior.listen().split(":")
print(addresses)
savior.send('got it, connecting!')
savior.close()

# first connection to helped server
helping_tcp = TcpClient(addresses[1], int(addresses[2]))
helping_tcp.send("I'm ready to help")
helping_udp = UdpClient(addresses[1], int(addresses[3]))
helping_udp.send("I'm ready to help but in udp")


def mouse_control():
    print('push b to stop control')
    try:
        while True:
            x, y = pyautogui.position()
            helping_udp.send(f'{x},{y}')
            time.sleep(0.05)
    except KeyboardInterrupt:
        print('controlled mouse mod has been turn off by user')


def send_voice():
    global addresses
    voice_sending = UdpClient(addresses[1], 9990)
    audio = pyaudio.PyAudio()
    voice_format = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024
    stream = audio.open(format=voice_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    # Continuously read audio from the microphone and send it to the server
    try:
        while True:
            data = stream.read(chunk)
            voice_sending.send(data)
    except:
        print('hanged up')
