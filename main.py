from data_manager import DataManager
from flight_search import FlightSearch
from email_manager import SendEmail

# Creating objects
data_manager = DataManager()
sheet_data = data_manager.get_from_sheet()
email_manager = SendEmail()

# Email message initialisation
message = ""

# Looping through flightdata and compare prices
for flight in sheet_data["taulukko1"]:
    flight_search = FlightSearch(flight)
    flight_info = flight_search.get_flight_info()["data"][0]
    if flight_info["price"] < flight["price"]:
        message += email_manager.append_to_message(flight_info)

# If found at least one price, that is lower than in sheet, send email
if message:
    email_manager.send_mail(message)
