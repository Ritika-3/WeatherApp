# 🌦 WeatherApp

A simple weather app built with **Python** and **Streamlit**. It fetches live data from the **OpenWeatherMap API** and shows you the current conditions along with forecasts. You can search by city, see temperature, humidity, wind, and even check the location on a map.

---

## ✨ What it does

* Search weather by **city name**
* Shows **current temperature, feels-like, humidity, pressure, wind**
* Weather condition with an icon (☁️ 🌤 🌧 etc.)
* Simple map view using latitude & longitude
* Results are cached for 10 minutes so you don’t spam the API
* Built with a clean UI using Streamlit

---

## 🛠 Tech Used

* **Python 3.10+**
* **Streamlit** for the interface
* **Requests** to talk to the API
* **python-dotenv** for handling the API key
* **Pandas** for quick data formatting and charts

---

## 📂 Project Layout

```
weather-app/
├── .env.example      # sample env file (API_KEY goes here)
├── requirements.txt  # dependencies
├── src/
│   ├── app.py        # Streamlit app (UI + logic)
│   ├── api.py        # functions that call the weather API
│   ├── utils.py      # helpers (unit conversion, time formatting)
└── README.md
```

---

## 🚀 Getting Started

1. Clone this repo:

   ```bash
   git clone https://github.com/<your-username>/weather-app.git
   cd weather-app
   ```

2. Create a virtual environment and install requirements:

   ```bash
   py -3.10 -m venv .venv
   .\.venv\Scripts\activate     # Windows PowerShell
   # or
   source .venv/Scripts/activate   # Git Bash / Linux / Mac

   pip install -r requirements.txt
   ```

3. Set up your API key:

   * Copy `.env.example` → `.env`
   * Put your OpenWeatherMap API key inside:

     ```
     API_KEY=your_openweather_api_key_here
     ```

4. Run the app:

   ```bash
   streamlit run src/app.py
   ```

---

## 📊 Example API Response

This is what a typical response from OpenWeatherMap looks like for Delhi:

```json
{
  "coord": { "lon": 77.2167, "lat": 28.6667 },
  "weather": [
    {
      "id": 804,
      "main": "Clouds",
      "description": "overcast clouds",
      "icon": "04d"
    }
  ],
  "main": {
    "temp": 31.38,
    "feels_like": 36.79,
    "pressure": 999,
    "humidity": 64
  },
  "visibility": 10000,
  "wind": { "speed": 2.03, "deg": 88 },
  "clouds": { "all": 100 },
  "sys": { "country": "IN", "sunrise": 1755303654, "sunset": 1755351016 },
  "timezone": 19800,
  "name": "Delhi",
  "cod": 200
}
```

---

## 🔎 How the app uses this

* `coord.lat` / `coord.lon` → to plot the city on the map
* `main.temp` / `main.feels_like` → to show the temperature and feels-like value
* `weather[0].description` + `weather[0].icon` → to display condition and an icon
* `wind.speed` → wind info
* `sys.sunrise` / `sys.sunset` → converted to readable times
* `name` + `sys.country` → location header

---

## 🔒 Note on security

Don’t commit your `.env` file. The real API key should stay private.
Commit only `.env.example` with placeholders so others know what they need to set up.

---
