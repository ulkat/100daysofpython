from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service()

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element("id", "cookie")
money = int(driver.find_element("id", "money").text)

store = driver.find_element("xpath", '//*[@id="store"]')
prices = store.find_elements("css selector", "div b")
list = []
for item in prices:
    temp = item.text.split("-")[1]
    print(temp)


# just_prices = [price.text.split("-") for price in prices]

# print(just_prices)

# for item in prices:
#     price = (item.text.split("-"))
#     print(price)


# print(just_prices)

#
# is_game_on = True
#
# while is_game_on:
#     cookie.click()

