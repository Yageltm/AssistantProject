import socket
import pyaudio
import keyboard

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Set parameters for audio stream
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

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
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# Continuously receive audio data from the client and play it
print('press d to hang up.')
while True:
    data = client_socket.recv(CHUNK)
    stream.write(data)
    if keyboard.is_pressed('d'):
        break


# Cleanup
stream.stop_stream()
stream.close()
audio.terminate()
client_socket.close()
server_socket.close()