### 📅 Day 33: ISS Overhead Notifier 🚀 & Kanye Quote Generator 🎤

Two projects today — one uses APIs to send email alerts when the ISS is overhead, and the other is a fun GUI that fetches random Kanye West quotes.

---

#### 🚀 ISS Overhead Notifier

A Python automation script that sends an email notification when the International Space Station (ISS) is flying above your location during nighttime.

#### 🧠 What It Does
- Retrieves the ISS’s current location using the Open Notify API  
- Determines local sunrise and sunset times via the Sunrise-Sunset API  
- Checks if the ISS is near your coordinates and it’s currently night  
- Sends an email alert if both conditions are true  
- Repeats the check every 60 seconds using a loop

#### 📝 What I Learned
- API Endpoints and Making API Calls  
- Handling Responses: HTTP Codes, Exceptions & JSON Data  
- API Parameters: Match Sunset Times with the Current Time  
- Time-based logic using `datetime`  
- Sending emails using `smtplib` with `starttls()`  
- Creating background loops with `while True` and `time.sleep()`

#### 💻 Example
![day33_iss-alert](https://github.com/user-attachments/assets/44fa907d-c28a-4b4a-9351-93b7da8d1add)


---

#### 🎤 Kanye Quote Generator *(Just for fun)*

A playful GUI app that shows random Kanye West quotes using the `kanye.rest` API.

#### 🧠 What It Does
- Sends a GET request to the Kanye REST API  
- Displays the quote in a canvas using `tkinter`  
- Updates the quote each time a custom image button is clicked

#### 🔁 Reinforced Concepts
- GUI creation with `tkinter`  
- Making API requests with `requests`  
- Parsing JSON data from a response  
- Updating text on canvas with `itemconfig()`  
- Using `PhotoImage` to load and display images

#### 💻 Example
![day33_kanye-says](https://github.com/user-attachments/assets/21e52241-78e9-41fd-b209-dce50d7f5570)

