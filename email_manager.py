import smtplib
import datetime as dt
import os


class SendEmail:
    def __init__(self):
        self.my_email = os.getenv("EMAIL")
        self.my_pass = os.getenv("EMAIL_PASS")

    def send_mail(self, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_pass)
            connection.sendmail(from_addr=self.my_email, to_addrs=self.my_email, msg=message)

    def parse_time(self, time):
        date_time_list = []
        date_time_str = time
        date_str, time_str = date_time_str.split("T")
        date = dt.datetime.strptime(date_str, "%Y-%m-%d").date()
        time = dt.datetime.strptime(time_str[:-5], "%H:%M:%S").time()
        date_time_list.append(date)
        date_time_list.append(time)
        return date_time_list

    def append_to_message(self, flight_json):
        message = "Subject: Flight deals\n\n"
        message += f'Price {flight_json["price"]} euros, '
        message += f'From {flight_json["cityFrom"]} '
        message += f"to {flight_json['cityTo']}.\n"
        message += f"Book tickets from {flight_json['deep_link']}\n"
        message += f'Departure {self.parse_time(flight_json["local_departure"])}\n\n'
        return message
