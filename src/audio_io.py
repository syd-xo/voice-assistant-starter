
import os
from pathlib import Path
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav

TEMP_DIR = Path("temp")

def ensure_temp_dir():
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

def record_to_file(filename: str, duration: float = 6.0, samplerate: int = 16000, channels: int = 1):
    """Record from the default microphone into a WAV file."""
    print(f"Recording {duration} seconds at {samplerate} Hz...")
    ensure_temp_dir()
    frames = int(duration * samplerate)
    audio = sd.rec(frames, samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()
    wav.write(filename, samplerate, audio)
    print(f"Saved: {filename}")

def play_wav(filename: str):
    import simpleaudio as sa
    print(f"Playing: {filename}")
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
