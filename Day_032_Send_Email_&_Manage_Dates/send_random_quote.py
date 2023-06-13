import smtplib
import datetime as dt
import random

EMAIL = ""
PASSWORD = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:

    with open("quotes.txt") as file:
        contents = file.read()
        quotes_list = contents.split("\n")
        random_quote = random.choice(quotes_list)
        print(random_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="alfei0410@yahoo.com",
            msg=f"Subject: Wednesday Motivation Quote\n\n{random_quote}"
        )
