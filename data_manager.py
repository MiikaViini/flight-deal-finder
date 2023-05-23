import requests
import os


class DataManager:
    def __init__(self):
        self.headers = {
            "Authorization": os.getenv("SHEETY_TOKEN")
        }

        self.api_endpoint = os.getenv("SHEETY_API_ENDPOINT")
        self.response_json = ""

    def edit_price(self, price, obj_id):
        parameters = {
            "taulukko1": {
                "price": price
            }
        }
        response = requests.put(url=f"{self.api_endpoint}/{obj_id}", json=parameters, headers=self.headers)
        self.response_json = response.json()
        return self.response_json

    def get_from_sheet(self):
        response = requests.get(url=self.api_endpoint, headers=self.headers)
        self.response_json = response.json()
        return self.response_json
