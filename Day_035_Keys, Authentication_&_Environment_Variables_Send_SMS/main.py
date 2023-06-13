import requests
from twilio.rest import Client


API_KEY = "the api key"
MY_LAT = 5.603717
MY_LONG = -0.186964
TW_NUM = "twilio number"
TW_AUTH = "twilio auth token"
TW_SID = "twilio sid"

account_sid = TW_SID
auth_token = TW_AUTH

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,alerts,minutely"
}


response = requests.get("https://api.openweathermap.org/data/2.8/onecall?", params=params)
response.raise_for_status()

accra_weather_data = response.json()["hourly"]
accra_weather_data_slice = accra_weather_data[:12]

will_rain = False
for hourly_data in accra_weather_data_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Likely to rain today. Carry an umbrella.",
        from_=TW_NUM,
        to=''
    )

    print(message.status)
