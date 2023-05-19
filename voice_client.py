import socket

import keyboard
import pyaudio


def send_voice(ip):
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set parameters for audio stream
    voice_format = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024

    # Create socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, 9990)
    client_socket.connect(server_address)

    # Open audio stream
    stream = audio.open(format=voice_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    # Continuously read audio from the microphone and send it to the server
    print('press d to hang up')
    try:
        while True:
            data = stream.read(chunk)
            client_socket.sendall(data)
            if keyboard.is_pressed('d'):
                client_socket.sendall('b')
    except:
        pass
    print('call ended')

