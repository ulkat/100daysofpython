import requests

tequila_endpoint = "https://api.tequila.kiwi.com"
tequila_headers = {
    "apikey": "dWgIPBPSgkk_ZLSO--0OxxFe5DO4jwsV"
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city_code = city
        self.query = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(
            url=f"{tequila_endpoint}/locations/query",
            headers=tequila_headers,
            params=self.query
        )
        self.result = response.json()["locations"]
        self.code = self.result[0]["code"]
        self.iata_code()

    def iata_code(self):
        self.city_code = self.code
