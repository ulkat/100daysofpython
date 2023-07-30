from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

MY_EMAIL = YOUR_EMAIL
MY_PASSWORD = YOUR_PASSWORD
SIMILAR_ACC = SIMILAR_ACC


class InstaFollower:
    def __init__(self):
        self.service = Service()
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(name="detach", value=True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.users = []

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(2)
        email_box = self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_box.send_keys(MY_EMAIL)
        password_box = self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_box.send_keys(MY_PASSWORD)
        password_box.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(4)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}/")
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}/followers/")
        time.sleep(2)
        modal = self.driver.find_element("xpath", '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements("css selector", "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element("xpath", '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
# insta_bot.follow()
