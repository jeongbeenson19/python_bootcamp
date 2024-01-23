import os
import requests
import datetime

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT_EXERCISE = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = "https://api.sheety.co/0e7fc498f0d5c4910a8153572760bad3/myWorksout의 사본/시트1"

GENDER = "man"
WEIGHT_KG = "120"
HEIGHT_CM = "192"
AGE = "22"
exercise_text = input("What do you do today? ")

# 사용자가 입력을 하지 않은 경우 처리
if not exercise_text:
    print("Please enter an exercise.")
    exit()

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

# Nutritionix API 응답 확인
if x_response.status_code != 200:
    print(f"Nutritionix API request failed with status code {x_response.status_code}")
    print(x_response.text)
    exit()

x_data = x_response.json()
print(x_data)

sheety_headers = {
    "Content-Type": "application/json",
}

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

# x_data가 비어있는 경우 예외 처리
if "exercises" not in x_data:
    print("No exercises found in the response.")
    exit()

for exercise in x_data["exercises"]:
    sheet_inputs = {
        "시트1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"],
            "duration": exercise.get("duration_min", ""),
            "calories": exercise.get("nf_calories", ""),
        }
    }


    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
    print(sheety_response.text)
