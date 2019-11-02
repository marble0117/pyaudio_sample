import numpy as np
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

window = np.hamming(CHUNK*CHANNELS)
freqList = np.fft.fftfreq(CHUNK*CHANNELS, d=1.0/RATE)

fig, ax = plt.subplots(figsize=(5, 3))
# ax.set(ylim=(-1, 1))
ax.axis([0, RATE/2, 0, 100])
line = ax.plot(np.array(list(range(CHUNK*CHANNELS))), np.zeros(CHUNK*CHANNELS))[0]


def update(i):
    data = stream.read(CHUNK)
    wave = np.frombuffer(data, dtype="int16") / float(2**15)
    window_wave = wave * window
    wave_dft = np.fft.fft(window_wave)
    windowedAmp = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in wave_dft]
    line.set_data(freqList, windowedAmp)


ani = FuncAnimation(fig, update, interval=1)
plt.draw()
plt.show()

stream.stop_stream()
stream.close()

p.terminate()