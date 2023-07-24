import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "3DRU5JOYPC40M7EZ"
NEWS_API_KEY = "cbf08997247749c48b108c4d90cadc18"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
 }

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

close_price_list = [value["4. close"] for (key, value) in data["Time Series (Daily)"].items()]
yesterday_price = float(close_price_list[0])
db_yesterday_price = float(close_price_list[1])
difference = abs(yesterday_price-db_yesterday_price)
perc = round(difference/yesterday_price * 100)
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
if perc > 5:
    news_parameters = {
        "q": COMPANY_NAME,
        "apikey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles_list = news_data["articles"]
    news_list = articles_list[0:3]
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{perc}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in news_list]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
