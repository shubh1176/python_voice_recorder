import pyaudio
import wave

frames_per_buffer1 = 3200
format1 = pyaudio.paInt16
channel1 = 1
rate1 = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format = format1,
    channels = channel1,
    rate = rate1,
    input = True,
    frames_per_buffer= frames_per_buffer1,
)
print("start recording ")
seconds = 5
frames = []
for i in range(0,int(rate1/frames_per_buffer1 * seconds)):
    data = stream.read(frames_per_buffer1)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav", "wb")
obj.setnchannels(channel1)
obj.setsampwidth(p.get_sample_size(format1))
obj.setframerate(rate1)
obj.writeframes(b"".join(frames))
obj.close()
p.terminate()


