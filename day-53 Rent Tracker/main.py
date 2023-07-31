from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import requests

ACCEPT_LANGUAGE = "en,tr-TR;q=0.9,tr;q=0.8,en-US;q=0.7"
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115"
              ".0.0.0 Safari/537.36 OPR/101.0.0.0")

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
}


response = requests.get('https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B"pagination"%3A%7B'
                        '%7D%2C"mapBounds"%3A%7B"north"%3A38.17515101321353%2C"east"%3A-122.13910189990234%2C"south"%'
                        '3A37.33587038492648%2C"west"%3A-123.01251498583984%7D%2C"regionSelection"%3A%5B%7B"regionId'
                        '"%3A20330%2C"regionType"%3A6%7D%5D%2C"isMapVisible"%3Afalse%2C"filterState"%3A%7B"price"%3A%7'
                        'B"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"m'
                        'ax"%3A3000%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"valu'
                        'e"%3Atrue%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"'
                        'value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%7D', headers=headers)
rent_web_page = response.text


soup = BeautifulSoup(rent_web_page, "html.parser")

a_tags = soup.select('[class*="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link"]')
all_prices = soup.find_all(attrs={"data-test": "property-card-price"})

prices = []
links = []
addresses = []


for price in all_prices:
    prices.append(price.text)


for a in a_tags:
    non_part = "https://www.zillow.com"
    a_href = a.get('href')
    if non_part not in a_href:
        final_href = non_part + a_href
    else:
        final_href = a_href

    links.append(final_href)
    addresses.append(a.getText())

print(links)
print(addresses)
print(prices)


service = Service()

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(service=service, options=options)

time.sleep(1)

for i in range(len(links)):
    time.sleep(2)
    driver.get("https://forms.gle/ThF7o26sqhkUEG6v5")

    address_box = driver.find_element("xpath",
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box = driver.find_element("xpath",
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_box = driver.find_element("xpath",
                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    send_button = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    time.sleep(1)

    address_box.send_keys(addresses[i])
    price_box.send_keys(prices[i])
    link_box.send_keys(links[i])
    send_button.click()


print("All addresses have been saved.")