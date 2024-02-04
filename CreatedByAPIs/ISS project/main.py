import requests
from datetime import datetime

MY_LAT = 37.175130
MY_LONG = 128.468330


parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Seoul"
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)
