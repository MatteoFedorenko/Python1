import requests
import json

response = requests.get("https://randomuser.me/api/")

data = response.json()

#Eliminate all data
with open("user.json", "w") as file:
    json.dump([], file)

#Save current data
with open("user.json", "w") as file:
    json.dump(data, file, indent=4)

print(
    data["results"][0]["name"]["title"],
    data["results"][0]["name"]["first"],
    data["results"][0]["name"]["last"]
)