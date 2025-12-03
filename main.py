import requests
from datetime import datetime
from twilio.rest import Client
import os

#Chennai
LAT = 13.0827
LON = 80.2707 


OPEN_METEO_Endpoint = "https://api.open-meteo.com/v1/forecast"


Weather_params = {
    "latitude":LAT,
    "longitude":LON,
    "hourly": "precipitation",
    "forecast_days":1,
    "timezone": "auto"
}

WORK_START_HOUR = 8
WORK_END_HOUR = 18

#--------------------------------

#TWILIO DETAILS
# TWILIO_SID = "AC7a31917d221053bede"
# TWILIO_AUTH_TOKEN = "5f65c578ab8f5c"
# TWILIO_PHONE_NUMBER = "+151549"    # Your Twilio number
# TARGET_PHONE_NUMBER = "+91956" 

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TARGET_PHONE_NUMBER = os.getenv("TARGET_PHONE_NUMBER")




def will_it_rain_during_work_hours(start_hour=8,end_hour=18):

    response = requests.get(OPEN_METEO_Endpoint,Weather_params)
    response.raise_for_status()
    data = response.json()
    
    times = data["hourly"]["time"]
    precipitation = data["hourly"]["precipitation"]

    today = datetime.now().date()


    for time_str, rain_mm in zip(times, precipitation):
        dt = datetime.fromisoformat(time_str)

        #check only between 8am to 6pm
        if dt.date() == today and start_hour <= dt.hour < end_hour:
            if rain_mm > 0:

                return True
    return False


def send_sms(message_body):
    client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body = message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=TARGET_PHONE_NUMBER
    )
    print("SMS sent. Twilio status:", message.status)
            
if __name__ == "__main__":
    if will_it_rain_during_work_hours(WORK_START_HOUR, WORK_END_HOUR):
        send_sms("☔ RAIN ALERT: It will rain sometime between 8 AM and 6 PM. Take an umbrella!")
    else:
        send_sms("No rain in work hours. No SMS sent.")