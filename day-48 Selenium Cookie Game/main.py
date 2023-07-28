from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.python.org")
menu_block = driver.find_elements("xpath", '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# i don't know why it gives me a list
list = menu_block[0].find_elements("tag name", "li")
# and this doesn't give me a list it gives a selenium webdrive
new_list = []

for li in list:
    new = li.text.split("\n")
    new_list.append(new)

upcoming_events = {new_list.index(item): {item[0]: item[1]} for item in new_list}
print(upcoming_events)

driver.quit()
