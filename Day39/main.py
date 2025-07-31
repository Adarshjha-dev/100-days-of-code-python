import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
ORIGIN_CITY_IATA = "LON"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_later = datetime.now() + timedelta(days=6 * 30)

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flight_data = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_later
    )
    cheapest = find_cheapest_flight(flight_data)

    if cheapest.price != "N/A" and cheapest.price < destination["lowestPrice"]:
        message = (
            f"✈️ Low price alert! Only £{cheapest.price} to fly from "
            f"{cheapest.origin_airport} to {cheapest.destination_airport}, "
            f"{cheapest.out_date} to {cheapest.return_date}."
        )
        notification_manager.send_telegram(message)
