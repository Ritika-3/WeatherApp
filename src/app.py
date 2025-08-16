import requests, os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import numpy as np
from api import fetch_weather
from datetime import datetime

load_dotenv()

st.set_page_config(page_title="Weather App", page_icon="⛅", layout="centered")
st.title("⛅ Simple Weather App")

city = st.text_input("City", key="city")

# st.write("This is the city you selected : ", city)


# cache requests for 10 minutes to avoid hitting limits
@st.cache_data(ttl=600)
def get_weather_bundle(city, units):
    data = fetch_weather(city=city, units=units)
    return {"data": data}

# --- Fetch & display ---

bundle = get_weather_bundle(city,"metric") 
d = bundle["data"]
# st.write(d)


#----
coords = d["coord"]
lat = d["coord"]["lat"]
lon = d["coord"]["lon"]
#---
weather = d["weather"][0]
weather_main = weather.get("main",0)
weather_desc = weather.get("description",0)
weather_icon = weather.get("icon")
weather_url = f"https://openweathermap.org/img/wn/{weather_icon}@2x.png"
#---
main = d["main"]
main_temp = main.get("temp",0)
main_feelsLike = main.get("feels_like",0)
main_tempMin = main.get("temp_min",0)
main_tempMax = main.get("temp_max",0)
main_pressure = main.get("pressure",0)
main_humidity = main.get("humidity",0)
main_seaLevel = main.get("sea_level",0)
main_tempMax = main.get("grnd_level",0)

#---
visibility = d["visibility"]
wind = d["wind"]
clouds = d["clouds"]
dt = d["dt"]
#---
sys = d["sys"]
sys_country = sys.get("country",0)
timezone = d["timezone"]
name = d["name"]

st.subheader(f"{name}, {sys_country}")

col1, col2 = st.columns([1,1])
with col1:
    st.image(weather_url, width=90)
    st.metric("Temperature", f"{round(main_temp)}", f"Feels {round(main_feelsLike)}")
    st.write(weather_desc)
with col2:
    st.write(f"**Humidity:** {main_humidity}%")
    st.write(f"**Pressure:** {main_pressure}hPa")
    st.write(f"**Sea Level:** {main_seaLevel} m")


df = pd.DataFrame({"lat": [lat], "lon": [lon]})

# show map
st.map(df, zoom=15, size=20, color="#0044ff")
