import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 5.603717
MY_LONG = -0.186964
MY_EMAIL = ""
PASSWORD = ""


def iss_alert():
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: ISS Alert\n\nLook up Faisal. The ISS is passing over you in the sky."
            )


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response2.raise_for_status()
    data = response2.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


send_iss_alert = True
iss_alert_printed = False

while send_iss_alert:
    current_time = datetime.now().hour
    is_night_time = is_night()

    if is_night_time and not iss_alert_printed:
        iss_alert()
        iss_alert_printed = True
        time.sleep(60)  # Add desired sleep duration here
    elif not is_night_time:
        iss_alert_printed = False
        time.sleep(60)
        iss_alert()