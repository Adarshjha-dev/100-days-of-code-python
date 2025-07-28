import os
import requests
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHAVANTAGE_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
daily_closes = [value for (key, value) in stock_data.items()]

latest_close_price = float(daily_closes[0]["4. close"])
previous_close_price = float(daily_closes[1]["4. close"])

price_difference = latest_close_price - previous_close_price
symbol = "🔺" if price_difference > 0 else "🔻"
percent_change = round((price_difference / previous_close_price) * 100)

articles = []
if abs(percent_change) > 1:
    news_query_params = {
        "q": COMPANY_NAME,
        "language": "en",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_query_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
news_messages = [
    f"{STOCK_NAME}: {symbol}{abs(percent_change)}% | {article['title']} - {article['description']}..."
    for article in articles
]


def telegram_bot_send_text(bot_message):
    send_text = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": bot_message,
        "parse_mode": "Markdown",
    }
    telegram_response = requests.post(send_text, data=payload)
    print("Telegram message sent:", telegram_response.status_code)
    return telegram_response.json()


for article in news_messages:
    telegram_bot_send_text(article)
