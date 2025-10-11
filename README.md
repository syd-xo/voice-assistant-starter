# Voice Assistant Starter Project  

An intelligent **voice assistant** that listens, understands, and speaks back, powered by **OpenAI Whisper** for speech recognition and **Coqui TTS** for natural-sounding speech.  

---

## Features
- **Speech Recognition** using Whisper  
- **Text Understanding** powered by Python NLP tools  
- **Realistic Voice Output** with Coqui TTS  
- Easy environment setup via **Conda**  
- Works seamlessly on **CPU or GPU**  
- Modular structure- simple to expand and customize  

---

## Requirements
Before you begin, make sure you have the following:
- **Python 3.10+**
- **Anaconda or Miniconda**
- A working **microphone** and **speakers**

---

## Setup Guide (Conda Method)

### 1. Create and Activate the Virtual Environment
```bash
conda create -n voice-assistant python=3.10 -y
conda activate voice-assistant
```

---

### 2. Install Dependencies

#### Core Libraries (CPU version)

```bash
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

If you have an NVIDIA GPU:
>
> ```bash
> conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
> ```

#### Other Project Requirements

```bash
pip install -r requirements.txt
```

---

### 3. Environment Variables
This project uses a `.env` file for configuration.  
When you clone the repo, you’ll see a `.env.example` file. This is your template.

- #### Create Your Own `.env` File
Copy the example file and rename it:
```bash
cp .env.example .env
````

- Then, edit the values inside `.env` as needed.

#### Example `.env`

```ini
# Whisper model size: tiny | base | small | medium | large
WHISPER_MODEL=base

# Coqui TTS model
COQUI_TTS_MODEL=tts_models/en/vctk/vits
# Optional speaker ID (if supported)
# COQUI_TTS_SPEAKER=p225
```

**Tips:**

* `tiny` or `base` - faster and lighter (ideal for laptops)
* `small`, `medium`, or `large` - slower but more accurate

**Important:**

For collaboration purposes, **DO NOT** push your `.env` file to GitHub, only `.env.example`.

---

### 4. Run the Project

Once everything is ready, launch your assistant:

```bash
python main.py
```

---

### 5. Verify PyTorch Installation
```bash
python -c "import torch, torchvision, torchaudio; print(torch.__version__, torchvision.__version__, torchaudio.__version__, torch.cuda.is_available())"
```

You should see something like:

```
2.5.1 0.20.1 2.5.1 False
```

---

## Notes

* Default setup uses **CPU** for better compatibility.
* Whisper and Coqui TTS models are downloaded automatically on first run.

---

## Credits

* **Speech Recognition:** [OpenAI Whisper](https://github.com/openai/whisper)
* **Text to Speech:** [Coqui TTS](https://github.com/coqui-ai/TTS)
* **Frameworks:** PyTorch, Torchaudio, Torchvision

---

## Future Enhancements

* Add chat-based conversation memory
* Support for multilingual speech recognition
* Integrate AI tools like OpenAI GPT or Rasa for smart responses

---
💗 Made with love and curiosity by Sydney Aisha 🌸