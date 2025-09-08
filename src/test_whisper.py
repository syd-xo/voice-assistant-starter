import whisper

# Load a small English model (faster)
model = whisper.load_model("small")

# Replace with a path to any audio file you have
audio_file = "output.wav"

# Transcribe audio
result = model.transcribe(audio_file)

print("Transcription:")
print(result["text"])
