from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import wave


CHUNK = 1024

wf = wave.open('wav/triangle.wav', 'rb')
fs = wf.getframerate()
channel = wf.getnchannels()
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=channel,
                rate=fs,
                output=True)

fig, ax = plt.subplots(figsize=(5, 3))
ax.set(ylim=(-1, 1))
line = ax.plot(np.array(list(range(CHUNK*channel))), np.zeros(CHUNK*channel))[0]


def update(i):
    data = wf.readframes(CHUNK)
    wave = np.frombuffer(data, dtype="int16") / float(2**15)
    if wave.shape[0] != channel*CHUNK:
        wave = np.pad(wave, (0, CHUNK*channel-wave.shape[0]), 'constant', constant_values=0)
    line.set_ydata(wave)
    stream.write(data)


ani = animation.FuncAnimation(fig, update, interval=1)
plt.draw()
plt.show()

stream.stop_stream()
stream.close()

p.terminate()
