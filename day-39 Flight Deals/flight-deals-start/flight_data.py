from datetime import datetime, timedelta
import requests
tequila_endpoint = "https://api.tequila.kiwi.com"
tequila_headers = {
    "apikey": "dWgIPBPSgkk_ZLSO--0OxxFe5DO4jwsV"
}
FLY_FROM ="IST"


from_time = datetime.now()
to_time = from_time + timedelta(days=180)




class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,iata_code):
        self.iata_code = iata_code


    def fligh_price(self):
        query = {
            "fly_from": FLY_FROM,
            "fly_to":  self.iata_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(
            url="https://tequila-api.kiwi.com/v2/search",
            headers=tequila_headers,
            params=query,
        )
        response.raise_for_status()

        try:
            result = response.json()["data"][0]
            return result["price"]

        except IndexError:
            return 999999
