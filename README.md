# ☔ Rain Alert – Day 35 of #100DaysOfCode

A fully automated **Rain Alert System** built in Python.  
Every morning at **7:00 AM**, the script checks if it will rain anytime between **8:00 AM and 6:00 PM** and sends me an SMS reminder to carry an umbrella.

The original course project used a different weather API that is no longer free, so I replaced it with the **Open-Meteo API**, which is fully free and requires no API key.

---

## 🚀 Features

- ✔ Fetches free weather data using **Open-Meteo**
- ✔ Checks rain only in the time window **(8 AM – 6 PM)**
- ✔ Sends automatic **SMS alerts via Twilio**
- ✔ Runs daily at **7:00 AM**
- ✔ Developed fully on **Linux (Ubuntu)**
- ✔ Deployed & scheduled on **PythonAnywhere**
- ✔ Secure API key handling (no secrets uploaded to GitHub)

---

## 🧰 Tech Stack

- **Python 3**
- **Open-Meteo API** (Weather forecast)
- **Twilio API** (SMS alerts)
- **Requests** library
- **PythonAnywhere Scheduler**
- **Linux (Ubuntu)** environment

---

## 📁 Project Structure

```bash
.
├── main.py             # Main script
├── requirements.txt    # Dependencies
├── .env.example        # Example of required environment variables
├── .gitignore          # Keeps secrets out of GitHub
└── README.md
If using a secrets_local.py file:

bash
Copy code
.
├── main.py
├── secrets_local.py    # Contains real sensitive keys (not committed)
├── requirements.txt
└── README.md
🔑 Environment Variables / Secrets
⚠ Never commit real API keys, tokens, or phone numbers to GitHub.

Option 1: Using .env (with python-dotenv)
Create a .env file:

env
Copy code
TWILIO_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+1XXXXXXXXXX
TARGET_PHONE_NUMBER=+91XXXXXXXXXX
LATITUDE=13.0827
LONGITUDE=80.2707
WORK_START_HOUR=8
WORK_END_HOUR=18
Add .env to .gitignore:

gitignore
Copy code
.env
Option 2: Using secrets_local.py
Create:

python
Copy code
# secrets_local.py
TWILIO_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "+1XXXXXXXXXX"
TARGET_PHONE_NUMBER = "+91XXXXXXXXXX"

LAT = 13.0827
LON = 80.2707

WORK_START_HOUR = 8
WORK_END_HOUR = 18
Add to .gitignore:

gitignore
Copy code
secrets_local.py
⚙️ How It Works
The script calls the Open-Meteo API to get today’s hourly precipitation forecast.

It filters hours between 8 AM and 6 PM.

If any hour has precipitation > 0 mm:

Twilio sends an SMS:
"☔ Rain alert: It may rain today between 8 AM and 6 PM. Carry an umbrella!"

If no rain:

No SMS is sent.

🖥️ Running Locally on Linux
Clone the repo:

bash
Copy code
git clone https://github.com/your-username/rain-alert.git
cd rain-alert
Create a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add your .env or secrets_local.py file.

Run the script:

bash
Copy code
python main.py
If rain is expected, you’ll receive an SMS.

☁️ Deploying to PythonAnywhere
Upload main.py, requirements.txt, and your secret file to PythonAnywhere.

Create a virtual environment and install dependencies:

bash
Copy code
pip install -r requirements.txt
Go to Tasks → Add a new scheduled task.

Set it to run at 07:00 AM IST
(PythonAnywhere runs in UTC, so schedule it at 01:30 UTC)

Command example:

bash
Copy code
cd /home/yourusername/projectfolder && /home/yourusername/.virtualenvs/yourenv/bin/python main.py
Your script will now run automatically every day.

🧪 Customization
Change latitude/longitude for your city

Change work time window (e.g., 9–17)

Replace SMS with:

Email

Telegram bot

WhatsApp (via Twilio)

📚 Learning Notes
Building this helped me practice:

Replacing deprecated APIs with modern alternatives

Using free weather data sources

Writing clean, modular code

Handling secrets safely

Scheduling automation tasks

Working entirely in Linux

Improving API + JSON parsing skills

🏷️ Tags
#python #automation #linux #api #twilio #openmeteo #pythonanywhere #100DaysOfCode
