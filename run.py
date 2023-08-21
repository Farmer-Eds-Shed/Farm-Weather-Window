import requests
import os
import json

lat = 53.6471
lon = -6.6967
api_key = os.getenv('OWM_API_KEY')
response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}")

data = json.loads(response.text)
print(data["list"])