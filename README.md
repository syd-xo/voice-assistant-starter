# Python Voice Assistant (Offline Speech-to-Text + Text-to-Speech)

A mini voice assistant built in Python using **Coqui TTS** (Text-to-Speech) and **OpenAI Whisper** (Speech-to-Text).  
It listens to the microphone, processes speech, and responds back with synthesized voice.  

## Features
- Live speech-to-text with Whisper   
- Natural text-to-speech with Coqui TTS 
- Runs locally, no OpenAI API required  
- Real-time conversation loop (assistant listens → responds → speaks back)

---

## Setup instructions 
1️⃣ Clone the repository

2️⃣ Create a virtual environment in Anaconda

3️⃣ Install dependencies 
  - python -m pip install --upgrade pip wheel
  - python -m pip install -r requirements.txt

4️⃣ Test the components 
  - Test the Text-to-Speech by running **python test_tts.py**. Generates **output.wav** if **simpleaudio** is installed.
  - Test the Speech-to-Text by running **python test_stt.py**. Records a short audio clip from your microphone and transcribes it using **Whisper**.

5️⃣ Run the voice assistant by running **python mini_voice_assistant.py**
  - The assistant will listen to your microphone in real-time and process audio in small chunks, responding with voice.

---

## Note
- If you close the conda environment, reactivate it with **conda activate voice-assistant** before running the voice assistant.
- For smoother responses, keep audio chunks short, with a 5-second wait time between each recording chunk.
- The voice assistant is currently set to use English.
- This project is still in development.


