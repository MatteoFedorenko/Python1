a={
    "res": [
        {"con": "IT","pon": 1},
        {"con": "PK1","pon": 2},
        {"con": "RUS","pon": 3}
    ]
}

try:
    if a["res"]["con"]["PK1"] != None:
        print("ok")
except:
    print("None", a["res"]["con"])

for option in a["res"]:

    if option["con"] == "PK":
        print(option["pon"])
        print("ok")
        break
   