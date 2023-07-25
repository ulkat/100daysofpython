#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.,
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

notification_manager = NotificationManager()

sheet_endpoint = "https://api.sheety.co/3a9acdcd4404986d85b1d5b375ac1863/flightDealsDosyasınınKopyası/prices"

response = requests.get(url=sheet_endpoint)
sheet_data = response.json()["prices"]
print(sheet_data)

for item in sheet_data:
    if item["iataCode"] == "":
        city = item["city"]
        object_id = (item["id"])
        flight_search = FlightSearch(city)
        iata_code = flight_search.city_code
        item["iataCode"] = iata_code
        data_manager = DataManager(iata_code, object_id)


for item in sheet_data:
    flight_data = FlightData(item["iataCode"])
    price = flight_data.fligh_price()
    if price < item['lowestPrice']:

        notification_manager.send_sms(
            message=f"Low price alert! Only £{price} to fly from IST  to {item['city']}-{item['iataCode']}."
        )
        pass


