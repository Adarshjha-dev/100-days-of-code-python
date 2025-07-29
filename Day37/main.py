import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Tracker",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu",
}

headers = {"X-USER-TOKEN": TOKEN}

# Create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? "),
}

# Create pixel

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "26",
}

# Update pixel
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)


delete_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

# Delete pixel
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
