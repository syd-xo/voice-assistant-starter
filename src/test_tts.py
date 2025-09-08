# test_tts.py

import sys

try:
    from TTS.api import TTS
except ModuleNotFoundError:
    print(
        "The 'TTS' package (Coqui TTS) is not installed in this environment.\n"
        "Activate your project environment and install dependencies from requirements.txt, e.g.:\n"
        "  conda activate <your-env>\n"
        "  python -m pip install --upgrade pip wheel\n"
        "  python -m pip install -r requirements.txt"
    )
    sys.exit(1)

try:
    import simpleaudio as sa
except ModuleNotFoundError:
    sa = None


def main():
    # Load a pre-trained TTS model (small English model)
    # Using explicit keyword for clarity and a quieter console
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

    text = "Hi! This is your computer speaking. Hello Sydney!"
    out_path = "output.wav"

    # Generate speech and save it to a file
    tts.tts_to_file(text=text, file_path=out_path)

    # Play the audio with simpleaudio if available
    if sa is not None:
        wave_obj = sa.WaveObject.from_wave_file(out_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    else:
        print(
            f"Audio saved to '{out_path}'. Install 'simpleaudio' if you want automatic playback:\n"
            "  python -m pip install simpleaudio"
        )


if __name__ == "__main__":
    main()
