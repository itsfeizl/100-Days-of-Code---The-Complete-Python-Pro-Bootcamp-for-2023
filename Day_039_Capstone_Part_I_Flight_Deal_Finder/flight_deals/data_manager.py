import requests
from pprint import pprint

# Get Data from Google Sheet
sheety_prices_endpoint = "https://api.sheety.co/053919c4ccf95f4aa4cdf5479ed69d2d/flightDealsFinder/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=sheety_prices_endpoint)
        self.destination_data = response.json()["prices"]

        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)