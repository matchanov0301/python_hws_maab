import requests

API_KEY = "b4b5cd0b45f60b3f49fc42d2b5a382d8"
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_desc.capitalize()}")
else:
    print("Error fetching weather data.")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {data}")
