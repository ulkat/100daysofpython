from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

# i didn't want to apply jobs instead i just saved them

service = Service()

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%"
           "2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
log_in_button = driver.find_element("xpath", "/html/body/div[1]/header/nav/div/a[2]")
log_in_button.click()

time.sleep(2)

email_input = driver.find_element("xpath", '//*[@id="username"]')
email_input.send_keys(MY_EMAIL)

password_input = driver.find_element("xpath", '//*[@id="password"]')
password_input.send_keys(MY_EMAIL)

log_in = driver.find_element("xpath", '//*[@id="organic-div"]/form/div[3]/button')
log_in.click()

time.sleep(1)

job_list = driver.find_element("xpath", '//*[@id="main"]/div/div[1]/div/ul')
all_jobs = job_list.find_elements("tag name", "li")

for job in all_jobs:
    job.click()
    try:
        save_button = driver.find_element("xpath", '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div'
                                               '/div[1]/div[1]/div[4]/div/button/span[1]')
    except:
        pass
    else:
        save_button.click()

    time.sleep(0.5)

