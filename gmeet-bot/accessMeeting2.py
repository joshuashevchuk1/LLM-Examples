import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

# === CONFIG ===
email = "joshuashevchuk9@gmail.com"
password = "Goaly67!!"
meeting_link = "https://meet.google.com/xxx-yyyy-zzz"  # Replace with actual Meet link

# === SETUP CHROME OPTIONS ===
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Auto allow mic/cam
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")

# Optional: Headless (if you don't need to see browser UI)
# chrome_options.add_argument("--headless")

# === START DRIVER ===
driver = uc.Chrome(options=chrome_options)

# === GO TO GOOGLE LOGIN ===
driver.get("https://accounts.google.com/signin")

time.sleep(2)

# Enter email
email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys(email)
email_input.send_keys(Keys.ENTER)

time.sleep(3)

# Enter password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

time.sleep(5)

# === OPEN MEETING LINK ===
driver.get(meeting_link)
time.sleep(7)

# === TURN OFF CAMERA ===
try:
    cam_button = driver.find_element(By.XPATH, "//div[@role='button'][@aria-label='Turn off camera (CTRL + E)']")
    cam_button.click()
except Exception as e:
    print("Camera button not found:", e)

# === TURN OFF MICROPHONE ===
try:
    mic_button = driver.find_element(By.XPATH, "//div[@role='button'][@aria-label='Turn off microphone (CTRL + D)']")
    mic_button.click()
except Exception as e:
    print("Mic button not found:", e)

time.sleep(2)

# === CLICK JOIN BUTTON ===
try:
    join_button = driver.find_element(By.XPATH, "//span[contains(text(),'Join now')]")
    join_button.click()
except Exception as e:
    print("Join button not found:", e)

print("✅ Bot joined the meeting!")

# === KEEP ALIVE ===
while True:
    time.sleep(60)  # Bot stays in meeting
