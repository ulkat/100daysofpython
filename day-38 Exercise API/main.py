import requests
from datetime import datetime
GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 179
AGE = 21

APP_ID = "YOUR ID"
API_KEY = "YOUR KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("What exercises you did today ?")

sheet_post_endpoint = "https://api.sheety.co/3a9acdcd4404986d85b1d5b375ac1863/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
     "query":exercise_text,
     "gender": GENDER,
     "weight_kg": WEIGHT_KG,
     "height_cm": HEIGHT_CM,
     "age": AGE
}

response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
result = response.json()
# print(result)

today = datetime.now()
today_in_formatted = today.strftime("%d/%m/%Y")
hour = today.strftime("%I:%M")

list = result["exercises"]
# print(list)

for exercise in list:
    exercise_Name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    sheet_params = {
        "workout": {
            "date": today_in_formatted,
            "time": hour,
            "exercise": exercise_Name,
            "duration": duration,
            "calories": calories
        }
    }
    sheet_response = requests.post(url=sheet_post_endpoint, json=sheet_params)


# i need to create some authentication
