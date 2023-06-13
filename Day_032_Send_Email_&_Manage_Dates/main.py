# import smtplib
# import random
#
# my_email = "faisal.alhassan61@gmail.com"
# password = "jkjhrdhclxxeqsev"

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.sendmail(
# #     from_addr=my_email,
# #     to_addrs="alfei0410@gmail.com",
# #     msg="Subject: Hello\n\nThis is the content of my email."
# # )
# # connection.close()
#
#
# # Alternatively:
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="alfei0410@gmail.com",
#         msg="Subject: Hello\n\nThis is the content of my email."
#     )


# Datetime
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_the_week = now.weekday()
hour = now.hour

date_of_birth = dt.datetime(year=1987, month=10, day=4, hour=13)
print(date_of_birth)