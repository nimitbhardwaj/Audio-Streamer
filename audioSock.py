import socket

class AudioSocket:
    def __init__(self, socket):
        self.socket = socket
        self.sample = None
    def arecv(self):
        CHUNK = 1024
        self.sample = self.socket.recv(CHUNK)
        return self.sample
    def sendSample(self, sample):
        CHUNK = 1024
        self.socket.send(sample)
