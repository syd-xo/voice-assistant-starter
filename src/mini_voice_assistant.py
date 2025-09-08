import whisper
from TTS.api import TTS
import sounddevice as sd
import numpy as np
import wavio
import simpleaudio as sa
import tempfile
import queue

# Parameters
sample_rate = 16000
chunk_duration = 5  # seconds per chunk

# Load models
print("Loading models...")
whisper_model = whisper.load_model("base")
tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)
print("Models loaded!")

# Queue for audio chunks
q = queue.Queue()


def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    q.put(indata.copy())


def record_and_transcribe():
    """Continuously record audio in chunks and transcribe."""
    with sd.InputStream(samplerate=sample_rate, channels=1, callback=audio_callback):
        print("Mini voice assistant is ready! Speak anytime. Say 'stop' to exit.")
        while True:
            frames = []
            for _ in range(int(sample_rate / 1024 * chunk_duration)):
                frames.append(q.get())
            audio_chunk = np.concatenate(frames, axis=0)

            # Save to temporary WAV file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
                wavio.write(tmpfile.name, audio_chunk, sample_rate, sampwidth=2)
                tmp_path = tmpfile.name

            # Transcribe
            result = whisper_model.transcribe(tmp_path)
            text = result["text"].strip()
            if text:
                print(f"You said: {text}")
                response = process_command(text)
                if response == "exit":
                    print("Goodbye!")
                    break
                speak_text(response)


def speak_text(text, file_name="response.wav"):
    tts_model.tts_to_file(text=text, file_path=file_name)
    wave_obj = sa.WaveObject.from_wave_file(file_name)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def process_command(text):
    text = text.lower()
    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! How are you today?"
    elif "name" in text:
        return "I am your mini voice assistant."
    elif "time" in text:
        from datetime import datetime
        return f"The time is {datetime.now().strftime('%H:%M')}."
    elif any(word in text for word in ["stop", "exit", "quit"]):
        return "exit"
    else:
        return "I’m listening. You can ask me something else!"



if __name__ == "__main__":
    record_and_transcribe()
