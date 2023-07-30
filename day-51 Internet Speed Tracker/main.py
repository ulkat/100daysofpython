from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = YOUR SPEED
PROMISED_UP = YOUR SPEED
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"
class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.promised_up = PROMISED_UP
        self.promised_down = PROMISED_DOWN
        self.service = Service()
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(name="detach", value=True)
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(2)
        start_test = self.driver.find_element("xpath", '//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                      'div[3]/div[1]/a')
        start_test.click()
        time.sleep(40)

        download_speed = float((self.driver.find_element("xpath", '//*[@id="container"]/div/div[3]/div/div/div/'
                                                            'div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div'
                                                           '[1]/div/div[2]/span')).text)
        upload_speed = float((self.driver.find_element("xpath", '//*[@id="container"]/div/div[3]/div/div/div/'
                                                           'div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div'
                                                           '[1]/div/div[2]/span')).text)
        self.up = upload_speed
        self.down = download_speed

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/?lang=tr")
        time.sleep(2)
        log_in_button = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/di'
                                                          'v/div[1]/div[1]/div/div[3]/div[5]/a')
        log_in_button.click()
        time.sleep(2)

        email_box = self.driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2'
                                                      ']/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/di'
                                                      'v/div[2]/div/input')
        email_box.send_keys(TWITTER_EMAIL)

        continue_button = self.driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div'
                                                            '/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        continue_button.click()
        time.sleep(2)

        password_box = self.driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div['
                                                         '2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/l'
                                                         'abel/div/div[2]/div[1]/input')
        password_box.send_keys(TWITTER_PASSWORD)
        password_box.send_keys(Keys.ENTER)
        time.sleep(2)

        tweet_box = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/d'
                                                      'iv/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/'
                                                      'div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/di'
                                                      'v/div/div/div')

        tweet_button = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                         'div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/d'
                                                         'iv[2]/div[2]/div/div/div[2]/div[3]')
        time.sleep(2)

        if self.up < self.promised_up or self.down < self.promised_down:
            tweet_box.send_keys(f"Merhaba TürkTelekom, bana vaad ettiğiniz internet hızı bu kadarken upload:"
                                f"{self.promised_up},download:{self.promised_down}, neden bu kadar alıyorum"
                                f" upload:{self.up},download:{self.down}? ")
            time.sleep(1)
            tweet_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
time.sleep(2)
bot.tweet_at_provider()
