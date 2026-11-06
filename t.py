import json

user = {
    "name": "Matvii",
    "age": 18
}

with open("user.json", "w") as file:
    json.dump(user, file)

