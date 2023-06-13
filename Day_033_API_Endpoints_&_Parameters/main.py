import requests
from datetime import datetime

MY_LAT = 5.603717
MY_LONG = -0.186964

params = {
    "my_lat": MY_LAT,
    "my_long": MY_LONG,
    "formatted": 0
}

response = requests.get(" https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

data = response.json()
data_results = data["results"]

sunrise_time = data_results["sunrise"]
sunrise_time_hour = (sunrise_time.split("T")[1]).split(":")[0]
print(f"Sunrise hour: {sunrise_time_hour}")

sunset_time = data_results["sunset"]
sunset_time_hour = sunset_time.split("T")[1].split(":")[0]
print(f"Sunset hour: {sunset_time_hour}")

time_now = datetime.now()
time_now_hour = time_now.hour
print(f"Hour right now: {time_now_hour}")


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
#
# response_status_code = response.status_code
# print(response_status_code)
#
# exception = response.raise_for_status()
# print(exception)
#
# # Get Data from API Endpoint
# data = response.json()
# print(data)
#
# # Get a Specific Data from API Endpoint
# iss_position = data["iss_position"]
# print(iss_position)
#
# # Get Latitude and Longitude positions from API Endpoint
# latitude = iss_position["latitude"]
# print(latitude)
# longitude = iss_position["longitude"]
# print(longitude)
#
# iss_position_tuple = (latitude, longitude)
#



