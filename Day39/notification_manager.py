import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.token = os.environ["TELEGRAM_BOT_TOKEN"]
        self.chat_id = os.environ["TELEGRAM_CHAT_ID"]
        self.api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def send_sms(self, message_body):
        response = requests.post(
            url=self.api_url,
            data={
                "chat_id": self.chat_id,
                "text": message_body
            }
        )
        if response.status_code != 200:
            print("Failed to send Telegram message:", response.text)
        else:
            print("Telegram message sent successfully")
