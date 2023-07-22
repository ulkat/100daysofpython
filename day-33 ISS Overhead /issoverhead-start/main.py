import requests
from datetime import datetime
import smtplib
MY_LAT = 41.059738
MY_LONG = 29.003455

my_email = "YOUREMAIL"
my_password = "YOUR PASSWORD"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def position():
    if iss_latitude < MY_LAT+5 and MY_LAT - 5 < iss_latitude and iss_longitude < MY_LONG+5 and MY_LONG-5 < iss_longitude:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if position():
    if time_now.hour <= sunrise or time_now.hour >= sunset:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="YOUR ADDRESS",
                                msg=f"Subject:Look Up!! \n\n If you look up right now you might see ISS!")
