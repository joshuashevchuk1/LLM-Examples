# requires ffmpeg (brew install ffmpeg)
import threading
from transformers import pipeline
from tqdm import tqdm

def show_loading():
    for _ in tqdm(range(100), desc="Loading ASR Model", bar_format="{l_bar}{bar}| {elapsed}"):
        if model_loaded:
            break

model_loaded = False
loading_thread = threading.Thread(target=show_loading)
loading_thread.start()

# Load the Whisper ASR model
asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-small")

# Stop the loading animation
model_loaded = True
loading_thread.join()

print("\n✅ =Model Loaded Successfully!")

audio_path = "test.m4a"
print("Transcribing audio...")
transcription = asr_pipeline(audio_path)
print("🎙️ Transcribed Text:", transcription["text"])
