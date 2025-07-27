import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MY_API_KEY")
account_sid = os.getenv("MY_ACCOUNT_SID")
auth_token = os.getenv("MY_AUTH_TOKEN")
to_number = os.getenv("TO_PHONE_NUMBER")
from_number = os.getenv("FROM_PHONE_NUMBER")

parameters = {
    "lat": 23.344101,
    "lon": 85.309563,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameters
)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️.",
        from_=from_number,
        to=to_number,
    )
    print(message.status)
