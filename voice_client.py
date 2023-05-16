import socket
import pyaudio

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Set parameters for audio stream
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Create socket and set server address
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9990)

# Open audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Continuously read audio from the microphone and send it to the server
try:
    while True:
        data = stream.read(CHUNK)
        client_socket.sendto(data, server_address)
except:
    print('Hanged up')

# Cleanup
stream.stop_stream()
stream.close()
audio.terminate()
client_socket.close()