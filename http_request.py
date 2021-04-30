import requests

response = requests.get('http://api.open-notify.org/astros.json')
result = response.json()

for person in result["people"]:
    print(person.get('name'))