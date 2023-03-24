from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")

# increase the volume by 6dB
audio = audio + 6
audio = audio * 1

audio = audio.fade_in(2000)

audio. export ("output.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("output.mp3")

print ("done")