import socket
import threading
import microphone
import audioSock

def getMyIP():
    mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySock.connect(('8.8.8.8', 80))
    ip = mySock.getsockname()[0]
    mySock.close()
    return ip

class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        ip = getMyIP()
        port = 6000
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSock.bind((ip, port))
        print 'My IP is ' + ip + ' and port used is ' + str(port)
        self.serverSock.listen(1)
        self.mic = microphone.Microphone()
        self.mic.start()

    def run(self):
        print 'listening'
        clientSock, addr = self.serverSock.accept()
        print 'I got the connection'
        aSock = audioSock.AudioSocket(clientSock)
        while True:
            sample = aSock.arecv()
            self.mic.playSample(sample)
            sample = self.mic.getSample()
            aSock.sendSample(sample)
