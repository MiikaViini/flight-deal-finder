import requests
import os
from date_manager import DateManager


class FlightSearch:
    def __init__(self, flight, dates):
        self.kiwi_headers = {
            "apikey": os.getenv("KIWI_APIKEY")
        }
        self.parameters = {
            "fly_from": "HEL",
            "fly_to": flight["iataCode"],
            "date_from": dates[0],
            "date_to": dates[1]
        }
        print(self.kiwi_headers["apikey"])
        self.get_flight_info()

    def get_flight_info(self):
        try:
            response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=self.kiwi_headers,
                                    params=self.parameters)
            response.raise_for_status()
            flight_json = response.json()
        except (KeyError, IndexError):
            print("no flights")
        else:
            return flight_json
