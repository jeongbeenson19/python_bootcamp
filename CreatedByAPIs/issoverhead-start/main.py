import requests
from datetime import datetime

MY_LAT = 37.175130 # Your latitude
MY_LONG = 128.468330
# Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Seoul"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
if -5 < iss_latitude - MY_LAT < 5 and -5 < iss_longitude - MY_LONG < 5:
    # and it is currently dark
    if not sunrise <= time_now.hour <= sunset:
        print("iss is over your head")
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



