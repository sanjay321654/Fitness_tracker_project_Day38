import requests
from datetime import datetime

API_ID = "4a3d5354"
API_KEY = "99829e326c1ff6105397a9a9960e271c"

GENDER = "male"
WEIGHT_KG = 55.22
HEIGHT_CM = 160.7
AGE = 20

sheety_endpoint = "https://api.sheety.co/c0cb2df7c00de3d0478db1b5b73eec19/workoutTrackerProject/sheet1"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
exercise_response.raise_for_status()

result = exercise_response.json()

today_date = datetime.now().strftime("%d/%m/%y")

now_time = datetime.now().strftime("%X")

# Construct the data for adding to Sheety
for exercise in result["exercises"]:
    sheety_data = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# Make the POST request to Sheety
sheety_response = requests.post(url=sheety_endpoint, json=sheety_data)
sheety_response.raise_for_status()

print(sheety_response.json())

