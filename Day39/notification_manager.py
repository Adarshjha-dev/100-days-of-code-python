import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"


class NotificationManager:
    def send_telegram(self, message):
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }

        response = requests.post(TELEGRAM_API_URL, data=payload)
        try:
            response.raise_for_status()
            print("✅ Telegram message sent successfully.")
        except requests.exceptions.RequestException as e:
            print("❌ Failed to send Telegram message.")
            print(e)
            print(response.text)
