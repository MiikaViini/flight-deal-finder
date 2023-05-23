# Flight deal finder
The Flight Deal Finder is a practical application developed as part of an Udemy course. This application, starting from day 40 of the course, leverages the powerful Kiwi API to search for affordable flights to pre-defined destinations. The app retrieves the destination information from a Google Sheet using the Sheety API.

The primary focus of this project is to provide hands-on experience with working with APIs and harnessing their capabilities. By utilizing the Kiwi API and integrating it with the Google Sheet through the Sheety API, learners gain valuable insights into API usage and learn how to leverage external data sources effectively.

# Usage
Per usual, clone repo like so:
```
git clone https://github.com/MiikaViini/flight-deal-finder.gitcd flight-deal-finder
```
Enter the repo and start script:
```
cd flight-deal-finder ; python3 main.py
```
## Prerequisites:
* Download the 'requests' module to enable API requests.
* Replace the provided API keys with your own, stored as environment variables for enhanced security.
* Follow your operating system's documentation to set up environment variables for the API keys.
* Configure your email account for programmatic access using instructions provided by Google or your email service provider.

# Documentation for the classes
## email_manager.py

`SendEmail` class handles sending emails using the `smtplib` library. It also utilizes the `datetime` module for working with dates and times and the `os` module for accessing environment variables.

The `SendEmail` class has an initialization method that retrieves the email address and password from environment variables and stores them in the `my_email` and `my_pass` attributes, respectively.

The `send_mail` method is responsible for sending an email. It establishes a connection with the SMTP server using the Gmail server address and port. It then sets up a secure connection using `starttls` and authenticates with the email address and password. Finally, it sends the email using the `sendmail` function, specifying the sender, recipient, and the message content.

The `parse_time` method is used to parse the date and time from a given string. It splits the string at the "T" delimiter and obtains the date and time strings. Using `strptime`, it converts the date string to a `datetime` object and the time string to a `time` object. The date and time objects are stored in a list and returned.

The `append_to_message` method is responsible for creating the email message content based on the flight information provided as `flight_json`. It constructs a string that includes the price, departure and destination cities, booking link, and departure time. It also utilizes the `parse_time` method to convert the departure time string into a formatted date and time representation. The message string is returned.

## date_manager.py

`DateManager` class manages dates for flight searches. It utilizes the `datetime` module for working with dates and times.

The `DateManager` class has an initialization method that initializes an empty list called `search_dates_list` to store search dates.

The `search_dates` method is responsible for generating the date range for flight searches. It obtains the current date and formats it as a string in the format "day/month/year" (kiwi api demands using this format) using `strftime`. The formatted date is then converted to a `datetime` object using `strptime`.

Next, it calculates the end date by adding 6 months (30 days multiplied by 6) to the start date using `timedelta`. The end date is also formatted as a string.

The start and end dates are appended to the `search_dates_list`, and the list is returned

## flight_search.py

`FlightSearch` class performs flight searches using the Kiwi API. It utilizes the `requests` library for making HTTP requests, the `os` module for accessing environment variables, and the `DateManager` class for managing dates.

The `FlightSearch` class has an initialization method that takes a `flight` parameter. It creates an instance of the `DateManager` class to manage dates for flight searches. The Kiwi API key is obtained from an environment variable and stored in the `kiwi_headers` attribute. The search parameters, including the departure airport code, destination airport code, and date range for the search, are stored in the `parameters` attribute.

The `get_flight_info` method is responsible for performing the flight search. It sends a GET request to the Kiwi API's search endpoint (`https://api.tequila.kiwi.com/v2/search`) with the appropriate headers and parameters. The response from the API is stored as JSON data in the `flight_json` variable.

If there are any exceptions during the API request (such as `KeyError` or `IndexError`), a "no flights" message is printed. Otherwise, the `flight_json` data is returned.

## data_manager.py

`DataManager` class  interacts with a web API using the `requests` library. The class provides methods for editing prices and retrieving data from a sheet.

The `DataManager` class has an initialization method that sets up the necessary credentials and endpoint for accessing the API. It stores the response from API calls as JSON data.

The `edit_price` method allows you to modify the price of an object identified by its ID. It takes the new price and the object's ID as parameters. Using the `requests` library, it sends a PUT request to the API endpoint with the updated price information, along with the necessary headers for authorization. The response from the API is stored and returned.

The `get_from_sheet` method retrieves data from the sheet by sending a GET request to the API endpoint with the appropriate headers for authorization. The response from the API, containing the sheet data, is stored and returned.
