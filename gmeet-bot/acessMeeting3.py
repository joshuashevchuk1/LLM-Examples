from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# --------------------------
# Use Your Existing Chrome Profile
# --------------------------
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/Users/joshuashevchuk/Library/Application Support/Google/Chrome Data")
chrome_options.add_argument("--profile-directory=Profile 10")

# Initialize Chrome driver with existing session
driver = webdriver.Chrome(options=chrome_options)

# --------------------------
# Go to Meeting (No Login Required)
# --------------------------
MEETING_URL = "https://meet.google.com/qaj-gvqw-pno"
driver.get(MEETING_URL)
print("Navigated to Google Meet...")

# OPTIONAL: Mute Mic and Camera (If needed)
# You can manually mute the microphone and camera if you want the bot to stay quiet

# Prevent script from exiting immediately
print("Bot is staying in the meeting...")

# Keep the browser session alive (infinite loop)
while True:
    time.sleep(60)  # Keep bot in meeting every 60 seconds
