import pyaudio
import threading

class Microphone(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sample = None
        self.inputSample = None
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
    def run(self):
        CHUNK = 1024
        while True:
            self.sample = self.stream.read(CHUNK)
            if self.inputSample == None:
                continue
            self.stream.write(self.inputSample, CHUNK)
        self.stream.stop_stream()
        self.stream.close()
        p.terminate()
    def playSample(self, sample):
        self.inputSample = sample
    def getSample(self):
        return self.sample

