import wave 
import matplotlib.pyplot as plt
import numpy as np

obj3 = wave.open("output.wav", "rb")

sample_freq = obj3.getframerate()
n_samples = obj3.getnframes()
signal = obj3.readframes(-1)

t_audio = n_samples/sample_freq

print(t_audio)

signal_arr = np.frombuffer(signal, dtype=np.int16)

times = np.linspace(0,t_audio, num = n_samples)

plt.figure(figsize=(15,5))
plt.plot(times, signal_arr)
plt.title("Audio Signal")
plt.show()