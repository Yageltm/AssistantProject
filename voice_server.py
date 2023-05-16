import socket
import pyaudio
import keyboard


def get_voice():
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set parameters for audio stream
    voice_format = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024

    # Create socket and start listening for client connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9990)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print('Server listening on port', 9990)

    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print('Client connected:', client_address)

    # Open audio stream
    stream = audio.open(format=voice_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk)

    # Continuously receive audio data from the client and play it
    print('press d to hang up.')
    while True:
        data = client_socket.recv(chunk)
        if data == 'b':
            break
        stream.write(data)
        if keyboard.is_pressed('d'):
            break
    print('call ended')



