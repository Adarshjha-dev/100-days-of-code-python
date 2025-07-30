import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load configuration

load_dotenv()

# Nutritionix credentials from environment variables

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety configuration

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
SHEET_USER = os.getenv("SHEET_USER")
SHEET_PASS = os.getenv("SHEET_PASS")

# User Profile data

GENDER = os.getenv("GENDER")
WEIGHT_KG = int(os.getenv("WEIGHT"))
HEIGHT_CM = int(os.getenv("HEIGHT"))
AGE = int(os.getenv("AGE"))

# Ask for exercise input

exercise_input = input("Tell me which exercises you did: ")

# Nutritionix headers and payload

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}

payload = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Make Nutritionix API call

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=payload, headers=headers)
result = response.json()
print(f"Nutritionix API result:\n{result}\n")

# Get current date and time

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

# Send each exercise entry to Sheety

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # Post to Sheety (Basic Auth)

    sheet_response = requests.post(
        url=SHEET_ENDPOINT, json=sheet_inputs, auth=(SHEET_USER, SHEET_PASS)
    )

    print(f"Sheety response:\n{sheet_response.text}")
