### 📅 Day 24: Mail Merge ✉️ & Snake Game High Score 🐍

Two mini-projects today — one automates personalized letters using mail merge, and the other improves a classic Snake game by adding persistent high score functionality.

---

#### 💌 Mail Merge Project

A lightweight automation script that generates personalized letters from a name list and a letter template.

#### 🧠 What It Does
- Reads a template letter with a `[name]` placeholder  
- Loads a list of names from a text file  
- Creates a unique letter for each name  
- Writes the output to individual text files, ready to send

#### 📝 What I Learned
- File handling using `open()`
- Dynamically creating and saving files using `with open(..., mode="w")`
- Relative and Absolute File Paths
- Looping through text files with `readlines()`  
- String manipulation using `replace()`  
- Managing input/output directory structures

#### 💻 Example
![Day24_mail-merge](https://github.com/user-attachments/assets/224e01d1-c2c9-43dd-b85e-fb2a004a5c5a)

---

#### 🐍 Snake Game Enhancement

Improved the existing Snake game by adding persistent high score functionality.

#### 🔧 What’s New
- High score now saved to a file and loaded each session  
- Score resets on collision, but high score remains  
- Enhanced the competitive aspect of the game

#### 💻 Example
![Day24_snake](https://github.com/user-attachments/assets/28ff755d-66ac-496d-ad47-bba61e261799)
