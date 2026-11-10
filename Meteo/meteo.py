import json
import requests
from datetime import datetime

def meteo():
    while True:
        print("Write a Country")
        try:
            askCountry = str(input("Answer: "))
        except:
            print("Wrong input!")
            print("Write a Country")
            askCountry = str(input("Answer: "))
        print("Write a City")
        try:
            askCity = str(input("Answer: "))
        except:
            print("Wrong input!")
            print("Write a City")
            askCity = str(input("Answer: "))

        response = requests.get("https://geocoding-api.open-meteo.com/v1/search?name="+askCity)
        data = response.json()

        with open("geo.json","w") as file:
            json.dump(data,file,indent=4)
        try:
            data["results"]
        except:
            meteo()
        for option in data["results"]:
            if option["country"] == askCountry:
                lat = option["latitude"]
                lon = option["longitude"]
                print(lat, lon)
                linkMeteo = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,rain,apparent_temperature,snowfall,is_day")
                dataM = linkMeteo.json()
                with open("meteo.json","w") as file:
                        json.dump(dataM,file,indent=4)

                try:
                    current = dataM["current"]
                    unit = dataM["current_units"]
                except:
                    meteo()

                print("======================================")
                print("Current weather:")

                time_str = current["time"]
                dt = datetime.fromisoformat(time_str)
                print(dt.strftime("%d/%m/%Y %H:%M"))
                print("⌛ Time:",dt.strftime("%d/%m/%Y %H:%M"))

                print("🌡️ Temperature:",current["temperature_2m"],unit["temperature_2m"])
                print("🌡️ Apparent Temperature:",current["apparent_temperature"],unit["apparent_temperature"])

                if current["is_day"] == 1:
                    print("☀️ Day:","Yes")
                elif current["is_day"] == 0:
                    print("🌑 Day:","No")

                print("🌧️ Rain:",current["rain"],unit["rain"])
                print("❄️ Snowfall:",current["snowfall"],unit["snowfall"])
                print("======================================")
                break
            else:
                print("Country search failed..")

meteo()
