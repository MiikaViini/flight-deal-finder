from data_manager import DataManager
from flight_search import FlightSearch
from email_manager import SendEmail
from date_manager import DateManager

# Creating objects
data_manager = DataManager()
date_manager = DateManager()
dates = date_manager.search_dates()
flight_sheet_data = data_manager.get_flights_from_sheet()
user_sheet_data = data_manager.get_users_from_sheet()
email_manager = SendEmail()

# Email message initialisation
message = ""

# Looping through flightdata and compare prices
for flight in flight_sheet_data["flights"]:
    flight_search = FlightSearch(flight, dates)
    flight_info = flight_search.get_flight_info()["data"][0]
    if flight_info["price"] < flight["price"]:
        message += email_manager.append_to_message(flight_info)

# If found at least one price, that is lower than in sheet, send email
if message:
    email_manager.send_mail(message, user_sheet_data)
