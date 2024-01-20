import requests
from api_key import API_KEY

URL = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "appid": API_KEY,
    "lat": 37.175130,
    "lon": 128.468330,
    "units": "metric"
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()
print(data)
