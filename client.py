import socket
import audioSock
import pyaudio
import threading
import microphone

class Client(threading.Thread):
    def __init__(self, IP, port):
        threading.Thread.__init__(self)
        self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSock.connect((IP, port))
        self.mic = microphone.Microphone()
        self.mic.start()
    def run(self):
        print 'connected'
        aSock = audioSock.AudioSocket(self.clientSock)
        while True:
            sample = self.mic.getSample()
            sample = pickle.dumps(sample)
            aSock.sendSample(sample)
            sample = aSock.arecv()
            sample = pickle.loads(sample)
            self.mic.playSample(sample)
