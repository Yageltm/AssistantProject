from tcp_client import TcpClient
from tcp_server import TcpServer
from udp_client import UdpClient
from udp_server import UdpServer
from voice_server import get_voice
from voice_client import send_voice
import pyaudio
import pyautogui
import time
from pynput import mouse

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


def on_click(x, y, button, pressed):
    if pressed:
        helping_udp.send(button.name)


def mouse_control():
    print('Push "b" to stop control')
    try:
        with mouse.Listener(on_click=on_click):
            while True:
                x, y = pyautogui.position()
                helping_udp.send(f'{x},{y}')
                time.sleep(0.5)
    except KeyboardInterrupt:
        print('Controlled mouse mode has been turned off by the user')


time.sleep(3)
send_voice(addresses[1])
