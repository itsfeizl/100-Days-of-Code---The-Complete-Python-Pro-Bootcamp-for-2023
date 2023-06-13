import requests
from twilio.rest import Client

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = ""
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "interval": "5min",
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_NUM = "+"
TWILIO_AUTH = ""
TWILIO_SID = ""

account_sid = TWILIO_SID
auth_token = TWILIO_AUTH

# STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# HINT 1:
# Get the closing price for yesterday and the day before yesterday.
# Find the positive difference between the two prices.
# e.g. 40 - 20 = -20, but the positive difference is 20.

# HINT 2:
# Work out the value of 5% of yesterday's closing stock price.

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)

tsla_stock_daily_data = stock_response.json()["Time Series (Daily)"]
tsla_data_list = [value for (key, value) in tsla_stock_daily_data.items()]

yesti_close = float(tsla_data_list[0]["4. close"])
day_before_yesti_close = float(tsla_data_list[1]["4. close"])

positive_diff = yesti_close - day_before_yesti_close
diff_percentage = (positive_diff / day_before_yesti_close) * 100

tsla_stock_direction = None
if positive_diff > 0:
    tsla_stock_direction = "🔺"
else:
    tsla_stock_direction = "🔻"

if abs(round(diff_percentage)) > 2:

    NEWS_API_KEY = ""
    news_params = {
        "q": STOCK,
        "searchIn": "title",
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
#
    news_articles_list = []
    for items in news_response.json()["articles"][:3]:
        news_articles_list.append(
            {"title": items["title"], "description": items["description"], "direction": tsla_stock_direction})
#
    for item in news_articles_list:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"News\n\n{STOCK}: {item['direction']}{round(diff_percentage)}% \n\nHeadline: {item['title']} \n\nBrief: {item['description']}",
                from_=TW_NUM,
                to=''
        )

        print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
