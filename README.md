# Mini-Data-Engineering-Project
## 🌊 Project Overview  This project demonstrates a mini data pipeline built in Python that processes user input (email), validates it, logs errors, and transforms valid data into a structured format.  It mimics real-world data engineering concepts like:  Input validation Data cleaning Error logging Pipeline orchestration

## ⚙️ Pipeline Architecture
<img width="281" height="333" alt="image" src="https://github.com/user-attachments/assets/b9a57876-a300-4108-84bc-677625110e9c" />

## 🧠 Core Features

## ✨ Modular Function Design
## ✨ Central Pipeline Orchestration
## ✨ File-based Logging System
## ✨ Data Cleaning & Transformation
## ✨ Real-time User Input Handling

## email_pipeline/
│
## ├── pipeline.py          # Main pipeline logic
## ├── Message log.txt     # Log file (auto-created/appended)
## └── README.md           # Project documentation

## 🔍 How It Works
1. Input Stage
Takes email input from user
## 2. Validation Stage
Checks:
Presence of @
Presence of .
## 3. Logging Stage
If invalid:
Appends error message to log file
## 4. Transformation Stage
If valid:
Cleans email (strip + lowercase)
Splits into:
username
domain
Returns structured dictionary
🧪 Example Run
✅ Valid Input
Input:
    abideenz095@gmail.com

Output:
    {'username': 'abideenz', 'domain': 'gmail.com'}
❌ Invalid Input
Input:
    abideenz095com

Output:
    Invalid Email: Log updated
📁 Log File Example
Invalid Email: Please enter a valid email
Invalid Email: Please enter a valid email
## 💻 Code Highlights
## 🔹 Pipeline Orchestration
def pipeline(Email):
    if not validate_email(user_email):
        write_log("Invalid Email: Please enter a valid email")
    else:
        cleaned_Email = clean_the_email(user_email)
        print(cleaned_Email)

        
## 🔹 Validation Logic
def validate_email(email):
    return '@' in email and '.' in email
    
## 🔹 Transformation Logic
def clean_the_email(email):
    clean_email = email.strip().lower()
    username, domain = clean_email.split('@')
    return {"username": username, "domain": domain}

