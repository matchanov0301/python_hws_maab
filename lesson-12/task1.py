from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, "html.parser")


table = soup.find("table")
rows = table.find("tbody").find_all("tr")


weather_data = []


for row in rows:
    columns = row.find_all("td")
    day = columns[0].text.strip()
    temperature = columns[1].text.strip().replace("°C", "")
    temperature = int(temperature)
    condition = columns[2].text.strip()


    weather_data.append({"day": day, "temperature": temperature, "condition": condition})


print("Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")


hottest_day = max(weather_data, key=lambda x: x["temperature"])
print(f"\nHottest Day: {hottest_day['day']} with {hottest_day['temperature']}°C")


sunny_days = []
for entry in weather_data:
    if entry["condition"] == "Sunny":
        sunny_days.append(entry["day"])

print("\nSunny Days:", ", ".join(sunny_days))


total_temperature = 0
for entry in weather_data:
    total_temperature += entry["temperature"]

average_temp = total_temperature / len(weather_data)
print(f"\nAverage Temperature: {average_temp:.2f}°C")