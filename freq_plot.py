from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import wave


CHUNK = 2048

wf = wave.open('wav/square.wav', 'rb')
fs = wf.getframerate()
channel = wf.getnchannels()
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=channel,
                rate=fs,
                output=True)

window = np.hamming(CHUNK*channel)
freqList = np.fft.fftfreq(CHUNK*channel, d=1.0/fs)

fig, ax = plt.subplots(figsize=(5, 3))
ax.axis([0, fs/2, 0, 100])
line = ax.plot(np.array(list(range(CHUNK*channel))), np.zeros(CHUNK*channel))[0]


def update(i):
    data = wf.readframes(CHUNK)
    wave = np.frombuffer(data, dtype="int16") / float(2**15)
    if wave.shape != window.shape:
        wave = np.pad(wave, (0, CHUNK*channel-wave.shape[0]), 'constant', constant_values=0)
    window_wave = wave * window
    wave_dft = np.fft.fft(window_wave)
    windowedAmp = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in wave_dft]
    line.set_data(freqList, windowedAmp)
    stream.write(data)

ani = animation.FuncAnimation(fig, update, interval=1)
plt.draw()
plt.show()

stream.stop_stream()
stream.close()

