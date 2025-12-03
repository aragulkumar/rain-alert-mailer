import requests
from datetime import datetime

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


# def will_it_rain_during_work_hours(start_hour=8,end_hour=18):


#     response = requests.get(OPEN_METEO_Endpoint,Weather_params)
#     response.raise_for_status()
#     data = response.json()
    


response = requests.get(OPEN_METEO_Endpoint,Weather_params)
response.raise_for_status()
data = response.json()

print(data)


