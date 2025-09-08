import whisper
import sounddevice as sd
import numpy as np
import wavio

# Parameters
duration = 5  # seconds
sample_rate = 16000  # Whisper works well with 16kHz

print("Recording... Speak now!")

# Record audio
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished

# Save to temporary WAV file
wavio.write("mic_input.wav", audio, sample_rate, sampwidth=2)
print("Recording saved as 'mic_input.wav'")

# Load Whisper model
model = whisper.load_model("small")

# Transcribe
result = model.transcribe("mic_input.wav")
print("\nTranscription:")
print(result["text"])
