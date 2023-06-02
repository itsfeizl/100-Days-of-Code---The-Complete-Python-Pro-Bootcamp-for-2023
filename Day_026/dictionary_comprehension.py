# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]
student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score > 50}
# print(passed_students)


# Challenge 1:
# You are going to use Dictionary Comprehension to create a dictionary called result
# that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:
words_list = sentence.split()
result = {word: len(word) for word in words_list}
# print(result)


# Challenge 2:
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that
# takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)


# Loop over a Pandas DataFrame

student_dict = {
    "students": ["Angela", "James", "Lilly"],
    "scores": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key, value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#
# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(index)
