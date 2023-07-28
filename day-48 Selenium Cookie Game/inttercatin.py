from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service()

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://secure-retreat-92358.herokuapp.com")

fname = driver.find_element("name", "fName")
fname.send_keys("Fahri")
lname = driver.find_element("name", "lName")
lname.send_keys("Ulkat")
email =driver.find_element("name", "email")
email.send_keys("fasfdas@gmail.com")
email.send_keys(Keys.ENTER)