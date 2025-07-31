### 📅 Day 39: Flight Deal Finder ✈️

A Python project that tracks flight prices and sends Telegram alerts when deals are found below a user-defined threshold.

#### 🧠 What It Does
- Fetches destination and price data from a Google Sheet  
- Uses the Amadeus API to retrieve IATA codes for cities  
- Searches for round-trip flights from London to multiple destinations  
- Filters results to find the cheapest available option  
- Sends real-time Telegram alerts when prices drop below the target  
- Updates missing IATA codes back to the Google Sheet

#### 📝 What I Learned
- Sending HTTP requests with rate limit handling (`time.sleep`)  
- Filtering and selecting optimal data from API responses  
- Sending push notifications through the Telegram Bot API
- Working with date ranges to search flights within specific time windows  
