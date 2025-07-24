### 📅 Day 32: Birthday Email Sender 🎂

A Python script that automatically sends personalized birthday emails to people on their special day using data from a CSV file.

#### 🧠 What It Does
- Reads a CSV file (`birthdays.csv`) containing names, emails, and birthdates  
- Checks if today's date matches any birthday in the dataset  
- Selects a random pre-written letter template  
- Replaces `[NAME]` placeholder with the actual name  
- Sends the customized message via email using SMTP

#### 📝 What I Learned
- Working with the `datetime` module  
- Sending emails securely using `smtplib` and `starttls()`  

#### 💻 Example
![Day32](https://github.com/user-attachments/assets/17a07ed7-06bf-4b51-a745-7ee697735b6d)
