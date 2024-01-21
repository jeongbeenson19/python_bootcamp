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

headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT_EXERCISE, json=parameters, headers=headers)

# 응답 확인
if response.status_code == 200:
    print("Success!")
    print(response.json())
else:
    print(f"Failed with status code {response.status_code}: {response.text}")
