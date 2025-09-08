
import os
from TTS.api import TTS

class CoquiTTS:
    def __init__(self, model_name: str | None = None, speaker: str | None = None):
        self.model_name = model_name or os.getenv("COQUI_TTS_MODEL", "tts_models/en/vctk/vits")
        # progress_bar=False avoids tqdm bars cluttering the console
        self.tts = TTS(model_name=self.model_name, progress_bar=False)
        self.speaker = speaker

        # Validate speaker if available
        try:
            if self.speaker and hasattr(self.tts, 'speakers'):
                if self.speaker not in (self.tts.speakers or []):
                    print(f"[Coqui] Speaker '{self.speaker}' not found in model. Using default.")
                    self.speaker = None
        except Exception:
            # Some models don't expose .speakers
            pass

    def synthesize_to_wav(self, text: str, out_path: str = "temp/reply.wav") -> str:
        if self.speaker:
            self.tts.tts_to_file(text=text, file_path=out_path, speaker=self.speaker)
        else:
            self.tts.tts_to_file(text=text, file_path=out_path)
        return out_path
