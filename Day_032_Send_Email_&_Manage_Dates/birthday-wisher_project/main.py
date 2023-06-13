import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = ""
PASSWORD = ""

# Get today's date
date_today = dt.datetime.now()

# Get birthdays
data = pandas.read_csv("birthdays.csv")
my_data = data.to_dict(orient="records")

# Check if today (day, month) matches a birthday in the birthdays.csv
for item in my_data:
    if 'day' in item and item['day'] == date_today.day and 'month' in item and item['month'] == date_today.month:
        # If it does, extract the name and email of the match
        NAME = item["name"]
        RECIPIENT_EMAIL = item["email"]

        # Pick a random letter from the letter_templates folder
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter = file.read().replace("[NAME]", NAME)

        # Send letter as email to the person whose birthday is today
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=RECIPIENT_EMAIL,
                    msg=f"Subject: Birthday Wishes\n\n{letter}"
                )
        except smtplib.SMTPAuthenticationError:
            print(f"There was an error of type: {smtplib.SMTPAuthenticationError}")
        else:
            print("Successful")
