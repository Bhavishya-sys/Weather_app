import requests
import json

city = input("Enter the name of city\n")


url = f"https://api.weatherapi.com/v1/current.json?key=5c3fd0bae8b942b5a6364438250710&q={city}"

r = requests.get(url)
print(r.text)
print(type(r.text))
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])