import requests
import api_key

lat = 53.6471
lon = 6.6967
api_key = api_key.api_key
response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}")
print(response.json())
print(api_key)
