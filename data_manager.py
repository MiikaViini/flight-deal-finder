import requests
import os


class DataManager:
    def __init__(self):
        self.headers = {
            "Authorization": os.getenv("SHEETY_TOKEN")
        }

        self.api_endpoint_flights = os.getenv("SHEETY_API_ENDPOINT_FLIGHTS")
        self.api_endpoint_users = os.getenv("SHEETY_API_ENDPOINT_USERS")
        self.response_json = ""

    def edit_price(self, price, obj_id):
        parameters = {
            "flights": {
                "price": price
            }
        }
        response = requests.put(url=f"{self.api_endpoint_flights}/{obj_id}", json=parameters, headers=self.headers)
        self.response_json = response.json()
        return self.response_json

    def get_flights_from_sheet(self):
        response = requests.get(url=self.api_endpoint_flights, headers=self.headers)
        self.response_json = response.json()
        return self.response_json

    def get_users_from_sheet(self):
        response = requests.get(url=self.api_endpoint_users, headers=self.headers)
        self.response_json = response.json()
        return self.response_json
