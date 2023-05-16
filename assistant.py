from tcp_client import TcpClient
from tcp_server import TcpServer
from udp_client import UdpClient
from udp_server import UdpServer
import pyautogui
import time

# first run to get calls for help
savior = TcpServer(8000)
print('ready to help')
data = savior.listen().split(":")
print(data)
savior.send('got it, connecting!')
savior.close()

# first connection to helped server
helping_tcp = TcpClient(data[1], int(data[2]))
helping_tcp.send("I'm ready to help")
helping_udp = UdpClient('localhost', int(data[3]))
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


mouse_control()
