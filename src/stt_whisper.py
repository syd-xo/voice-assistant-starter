
import whisper
from typing import Optional

class WhisperSTT:
    def __init__(self, model_name: str = "base"):
        # Load once
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str, language: Optional[str] = None) -> str:
        result = self.model.transcribe(audio_path, language=language)
        text = result.get('text', '').strip()
        return text
