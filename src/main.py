
import os
import time
from pathlib import Path
from dotenv import load_dotenv

from config import settings
from audio_io import record_to_file, play_wav, ensure_temp_dir
from stt_whisper import WhisperSTT
from tts_coqui import CoquiTTS
from assistant_brain import respond


def main():
    # Load environment
    load_dotenv()
    ensure_temp_dir()

    # Initialize engines
    print("Loading Whisper STT model:", settings['WHISPER_MODEL'])
    stt = WhisperSTT(model_name=settings['WHISPER_MODEL'])

    print("Loading Coqui TTS model:", settings['COQUI_TTS_MODEL'])
    tts = CoquiTTS(model_name=settings['COQUI_TTS_MODEL'],
                   speaker=settings.get('COQUI_TTS_SPEAKER'))

    print("\nReady! Press Enter to record, or type 'q' then Enter to quit.")
    while True:
        cmd = input("\nPress Enter to record 6s... (or 'q' to quit): ").strip().lower()
        if cmd == 'q':
            print("Goodbye!")
            break

        input_path = Path("temp/input.wav")
        reply_path = Path("temp/reply.wav")

        # 1) Record audio
        record_to_file(str(input_path), duration=6, samplerate=16000)

        # 2) Transcribe
        print("Transcribing...")
        try:
            text = stt.transcribe(str(input_path))
        except Exception as e:
            print("Transcription error:", e)
            continue

        print(f"You said: {text!r}")

        if not text:
            print("Heard nothing. Try again.")
            continue

        # 3) Assistant brain
        reply_text = respond(text)
        print("Assistant:", reply_text)

        # 4) TTS synth & play
        try:
            tts.synthesize_to_wav(reply_text, out_path=str(reply_path))
            play_wav(str(reply_path))
        except Exception as e:
            print("TTS/playback error:", e)


if __name__ == "__main__":
    main()
