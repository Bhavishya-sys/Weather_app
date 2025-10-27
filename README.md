The Weather App is a simple Python program that fetches and displays the current temperature of any city using the WeatherAPI.
It demonstrates how to work with REST APIs, JSON data, and HTTP requests using the requests library.

This project is perfect for beginners learning how to interact with APIs in Python.

🧠 How It Works

The user enters the name of a city (e.g., London, Delhi, New York).

The program sends a GET request to the WeatherAPI with your API key.

The API returns a JSON response containing live weather data.

The program extracts and displays the current temperature in Celsius.
🚀 Features

✅ Fetches real-time weather data 🌤️
✅ Displays temperature in Celsius 🌡️
✅ Uses WeatherAPI (free API)
✅ Demonstrates how to parse JSON responses
✅ Simple, fast, and beginner-friendly

🧰 Requirements

Python 3.x

requests module
Install it using:

pip install requests

🔑 API Setup

You can get a free API key from WeatherAPI.com
.

Sign up on their website.

Copy your API key.

Replace your key inside the URL:

url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
