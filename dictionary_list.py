contacts = {
    "number": "5",
    "data": [
        { "name": "Pepe"},
        { "last_name": "Clau"}
    ]
}

for data in contacts["data"]:
    if data.get("name") != None:
        print('this is the name', data["name"])
    if data.get("last_name") != None:
        print('this is the last name', data["last_name"])