import datetime as dt
import random
import smtplib

my_email = "your email"
password = "YOUR PASSWORD"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as file:
       quotes_list = file.readlines()

    random_quotes = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="YOUR ADRESS",
                            msg=f"Monday Motivatio!\n\n {random_quotes}")

