import os
import requests

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT_EXERCISE = 'https://trackapi.nutritionix.com/v2/natural/exercise'

GENDER = "man"
WEIGHT_KG = "120"
HEIGHT_CM = "192"
AGE = "22"
exercise_text = "i swam for a hour"

x_headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

x_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

x_response = requests.post(url=NUTRITIONIX_ENDPOINT_EXERCISE, json=x_parameters, headers=x_headers)

# 응답 확인
if x_response.status_code == 200:
    print("Success!")
    print(x_response.json())
else:
    print(f"Failed with status code {x_response.status_code}: {x_response.text}")

# sheety_endpoints = "https://api.sheety.co/0e7fc498f0d5c4910a8153572760bad3/myWorksout의 사본/시트1"
# }
#
# data = {
#
# }
#
# sheety_response = requests.post(url=sheety_endpoints,)