
import os

def _getenv(key: str, default: str | None = None) -> str | None:
    val = os.getenv(key, default)
    return val

settings = {
    "WHISPER_MODEL": _getenv("WHISPER_MODEL", "base"),
    "COQUI_TTS_MODEL": _getenv("COQUI_TTS_MODEL", "tts_models/en/vctk/vits"),
    "COQUI_TTS_SPEAKER": _getenv("COQUI_TTS_SPEAKER", None),
}
