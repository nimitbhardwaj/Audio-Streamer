import pyaudio
import threading

class Microphone(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        CHUNK = 1024
        RATE = 44100
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        p = pyaudio.PyAudio()
        self.stream = p.open(format = FORMAT,
                        channels = CHANNELS,
                        rate = RATE,
                        input = True,
                        output = True,
                        frames_per_buffer = CHUNK)
        self.sample = self.stream.read(CHUNK)
        self.inputSample = self.stream.read(CHUNK)
        self.kapa = self.inputSample
    def run(self):
        CHUNK = 1024
        kapa = self.inputSample
        while True:
            self.sample = self.stream.read(CHUNK)
            if self.inputSample == self.kapa:
                continue
            self.stream.write(self.inputSample, CHUNK)
        self.stream.stop_stream()
        self.stream.close()
        p.terminate()
    def playSample(self, sample):
        self.inputSample = sample
    def getSample(self):
        return self.sample

