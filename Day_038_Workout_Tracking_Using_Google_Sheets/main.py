import requests
from datetime import datetime
import os

APP_ID = os.environ.get("NUTRIX_APP_ID")
API_KEY = os.environ.get("NUTRIX_API_KEY")

query = input("What exercise did you do? ")
# gender = input("Are you male or female? ")
# weight = float(input("How much do you weigh (in kg)? "))
# height = float(input("How tall are you (in cm)? "))

# Get exercise information
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
ex_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
exercise_params = {
     "query": query,
     "gender": "male",
     "weight_kg": 72.5,
     "height_cm": 167.64,
     "age": 30
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=ex_headers)
print(response.json())
exercise = response.json()["exercises"][0]["user_input"]
exercise_duration = response.json()["exercises"][0]["duration_min"]
calories = response.json()["exercises"][0]["nf_calories"]
print(f"Exercise: {exercise}, Time: {exercise_endpoint}, Calories Burned: {calories}")


# Write exercise data to Google Sheets

today = datetime.now()
print(today)
date_string = today.strftime("%d/%m/%Y")
time_string = today.strftime("%X")

sheety_endpoint = 'https://api.sheety.co/56db0912c86bdb7369f071d62daa69dc/myWorkoutsCopy/workouts'
sheety_headers = {"Authorization": "Bearer MyName=Faisal+Alhassan"}
sheety_params = {
    "workout": {
        "date": date_string,
        "time": time_string,
        "exercise": exercise.title(),
        "duration": exercise_duration,
        "calories": calories
    }
}

response_a = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
print(response_a.json())
