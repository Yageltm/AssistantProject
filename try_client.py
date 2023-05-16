import socket
import pyaudio

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Set parameters for audio stream
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Create socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9990)
client_socket.connect(server_address)

# Open audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Continuously read audio from the microphone and send it to the server
try:
    while True:
        data = stream.read(CHUNK)
        client_socket.sendall(data)
except:
    print('hanged up')

# Cleanup
stream.stop_stream()
stream.close()
audio.terminate()
client_socket.close()