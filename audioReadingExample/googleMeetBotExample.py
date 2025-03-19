import subprocess
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# --------------------------
# Configuration
# --------------------------
# Replace with your actual Google Meet link
MEETING_URL = "https://meet.google.com/xms-ydgb-cyx"

# For Linux using PulseAudio capture:
# Adjust the input device if needed (e.g. a dedicated virtual sink)
FFMPEG_CMD = [
    "ffmpeg",
    "-f", "avfoundation",      # AVFoundation is the input system for macOS
    "-i", ":0",                # ":0" selects the default audio input device
    "-ac", "2",                # Two audio channels
    "-ar", "44100",            # Audio sample rate
    "output.wav"               # Output file
]

# FFMPEG_CMD = [
#     "ffmpeg",
#     "-f", "pulse",      # Using PulseAudio (Linux)
#     "-i", "default",    # Capture the default PulseAudio source; adjust if needed
#     "-ac", "2",         # Two audio channels
#     "-ar", "44100",     # Audio sample rate
#     "output.wav"        # Output file; you can also pipe or stream this
# ]

# For Windows using WASAPI, you might use a command like:
# FFMPEG_CMD = [
#     "ffmpeg",
#     "-f", "dshow",
#     "-i", "audio=Your_Audio_Device_Name",  # Replace with the correct device name
#     "output.wav"
# ]

# --------------------------
# Selenium Setup (Headless Chrome)
# --------------------------
chrome_options = Options()
# Use Chrome’s new headless mode which may support audio (requires a recent Chrome version)
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Auto-allow microphone access
chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# Optionally, specify additional flags to route audio to the expected device

# Initialize the Chrome driver (ensure chromedriver is installed and in your PATH)
driver = webdriver.Chrome(options=chrome_options)

# --------------------------
# Join Google Meet
# --------------------------
driver.get(MEETING_URL)
print("Joining Google Meet in headless mode...")

# Wait for the meeting page to load fully
time.sleep(5)  # Adjust delay as necessary

# --------------------------
# Start FFmpeg to Capture Audio
# --------------------------
print("Starting audio capture with FFmpeg...")
ffmpeg_proc = subprocess.Popen(FFMPEG_CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def monitor_ffmpeg():
    """Monitor FFmpeg output for debugging."""
    for line in iter(ffmpeg_proc.stderr.readline, b''):
        print(line.decode('utf-8').strip())

# Start a thread to monitor FFmpeg output (optional)
ffmpeg_monitor = threading.Thread(target=monitor_ffmpeg, daemon=True)
ffmpeg_monitor.start()

print("Audio capture is running. Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping audio capture and closing browser...")
    ffmpeg_proc.terminate()  # Stop FFmpeg
    driver.quit()
