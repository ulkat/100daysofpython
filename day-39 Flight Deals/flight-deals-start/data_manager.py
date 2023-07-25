import requests

sheet_endpoint = "https://api.sheety.co/3a9acdcd4404986d85b1d5b375ac1863/flightDealsDosyasınınKopyası/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, iata_code, object_id):
        self.iata_Code = iata_code
        self.object_id = object_id
        self.endpoint = f"{sheet_endpoint}/{object_id}"
        self.update_sheet()

    def update_sheet(self):
        parameters = {
            "price": {
                "iataCode": self.iata_Code

            }

        }
        requests.put(url=self.endpoint, json=parameters)



