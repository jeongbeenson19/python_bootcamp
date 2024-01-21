import requests
from api_key import API_KEY
from twilio.rest import Client

URL = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = "ACae3d19c1a66d05a51ede9f3777193b50"
auth_token = "d23069589a8f87043a6d6117e22fa706"

parameters = {
    "appid": API_KEY,
    "lat": 37.175130,
    "lon": 128.468330,
    "units": "metric",
    "exclude": "current,minutely,daily"
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_='+19048754780',
            to='+82 10 4619 3165'
        )
    print(message.status)
