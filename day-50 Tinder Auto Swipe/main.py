from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"


service = Service()

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://tinder.com/")

time.sleep(1)


sign_in = driver.find_element("xpath", '//*[@id="q-620494849"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
sign_in.click()

time.sleep(2)

with_fb = sign_in.find_element("xpath", '//*[@id="q1946091371"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
with_fb.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)


email_input = driver.find_element("xpath", '//*[@id="email"]')
email_input.send_keys(MY_EMAIL)

password_input = driver.find_element("xpath", '//*[@id="pass"]')
password_input.send_keys(MY_PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(2)

driver.switch_to.window(base_window)
time.sleep(3)

location = driver.find_element("xpath", '//*[@id="q1946091371"]/main/div[1]/div/div/div[3]/button[1]')
location.click()
time.sleep(3)

notifications = driver.find_element("xpath", '//*[@id="q1946091371"]/main/div[1]/div/div/div[3]/button[2]')
notifications.click()
time.sleep(3)

cookies = driver.find_element("xpath", '//*[@id="q-620494849"]/div/div[2]/div/div/div[1]/div[2]/button')
cookies.click()
time.sleep(3)

def left():
    try:
        left_button = driver.find_element("xpath", '//*[@id="q-620494849"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')
        left_button.click()

    except:
        pass



is_bot_on = True

while is_bot_on:
    left()
    time.sleep(2)
