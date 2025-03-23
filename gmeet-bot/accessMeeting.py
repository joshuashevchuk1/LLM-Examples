import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --------------------------
# CONFIGURATION
# --------------------------
EMAIL = "joshuashevchuk9@gmail.com"  # Replace with your email
PASSWORD = "Goaly67!!"      # Replace with your password
MEETING_URL = "https://meet.google.com/gse-useg-nta"

# --------------------------
# Selenium Setup
# --------------------------
chrome_options = Options()
# Keep Chrome visible for debugging
chrome_options.add_argument("--user-data-dir=/Users/joshuashevchuk/Library/Application Support/Google/Chrome Data")
chrome_options.add_argument("--profile-directory=Profile 1")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Auto allow mic/cam

# Initialize Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# --------------------------
# 1. Google Login
# --------------------------
print("Logging into Google...")

driver.get("https://accounts.google.com/signin")

# Input email
email_input = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.ID, "identifierId"))
)
time.sleep(5)

email_input.send_keys(EMAIL)
email_input.send_keys(Keys.ENTER)

time.sleep(5)

# Input password
password_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

print("Logged in successfully.")

# --------------------------
# 2. Navigate to Google Meet
# --------------------------
time.sleep(5)  # Let login complete
driver.get(MEETING_URL)
print("Navigated to Google Meet...")

# --------------------------
# 3. Join Meeting
# --------------------------
try:
    # Wait for "Join now" button to appear
    join_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Join now")]/parent::button'))
    )
    time.sleep(2)
    join_button.click()
    print("Joined the meeting successfully!")
except Exception as e:
    print("Failed to click Join Now:", e)

print("Bot is now in the meeting. Ctrl+C to stop.")

# Keep browser open
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Closing browser...")
    driver.quit()
