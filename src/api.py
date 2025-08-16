import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY=os.getenv("API_KEY")

ONECALL_URL="https://api.openweathermap.org/data/2.5/weather"

class ApiError(Exception):
    pass

def fetch_weather(city: str, units: str = 'metric'):
    params = {"q": city, "units": units, "appid": API_KEY} 
    r = requests.get(ONECALL_URL, params=params, timeout=10)
    if r.status_code == 401:
        raise ApiError("Unauthorized (401). New API keys can take ~1–2 hours to activate.")
    r.raise_for_status()
    return r.json()   