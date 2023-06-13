import requests

params = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=params)
question_data = response.json()["results"]

# Create a new file 'my_data.py' and populate it with a list of five dictionary elements whose
# key and value elements will be question and answer
with open("my_data.py", "w") as file:
    file.write("question_data = [")
    for x in range(0, 10):
        file.write("{'question': '" + response.json()['results'][x]['question'] + "','correct_answer': '" + response.json()['results'][x]['correct_answer'] + "'},")
    file.write("]")