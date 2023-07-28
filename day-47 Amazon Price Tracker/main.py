import requests
from bs4 import BeautifulSoup
import smtplib
ACCEPT_LANGUAGE = "en,tr-TR;q=0.9,tr;q=0.8,en-US;q=0.7"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)" \
             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"
BUY_PRICE = 60
my_email = "YOUR EMAIL"
my_password = "YOUR PASSWORD"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}
response = requests.get(url="https://www.amazon.com.tr/gp/product/B07L7Q6RGJ/ref=ox_sc_act_title_2?smid=A1UNQM1SR2CHM&psc=1",
             headers=headers)

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

price =(soup.find(name="span", class_="a-offscreen").getText())
price_wo_tl = price.replace("TL", "")
final_price = price_wo_tl.replace(",", ".")

# print(price)
# print(price_wo_tl)
# print(final_price)
# print(float(final_price))

if float(final_price) < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="YOUR ADDRESS",
                            msg=f"The product price is now {price}.")

#upload this code to cloud and run it every day
