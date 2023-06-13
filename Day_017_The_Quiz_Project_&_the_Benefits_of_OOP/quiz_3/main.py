from data import general_knowledge, history, geography, science_and_nature
from question_model import Question
from quiz_brain import QuizBrain
import random
import os

clear = lambda: os.system('cls')

print()
# list = random.sample(general_knowledge["difficult"], 10)
# print(list)
# print()
# print()
category = input("Welcome to the Quiz Game. Choose category: \nA. General Knowledge\nB. History\n\nEnter option 'A' or 'B': ").lower()
print()

choose_level = input("Choose difficulty level (Easy/Medium/Difficult): ").lower()

clear()
general_knowledge_qtn_list = random.sample(general_knowledge[choose_level], 10)
# geography_qtn_list = random.sample(geography[choose_level], 10)
history_qtn_list = random.sample(history[choose_level], 10)
# science_and_nature_qtn_list = random.sample(science_and_nature[choose_level], 10)


if category == "a":
    question_data = general_knowledge_qtn_list
elif category == "b":
    question_data = history_qtn_list
# elif category == "c":
#     # question_data = geography_qtn_list
# elif category == "d":
#     # question_data = science_and_nature



question_bank = []

for item in question_data:
    question = Question(item["question"], item["correct_answer"], item["remark"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)


print()
while quiz.still_has_questions():
    quiz.next_question()

if quiz.score == 10:
    remarks = "Perfect!"
elif quiz.score > 7 and quiz.score < 10:
    remarks = "Very Impressive!"
elif quiz.score > 5 and quiz.score < 7:
    remarks = "Good."
else:
    remarks = "Poor."

clear()
print("You've completed the quiz.")
print(f"You've answered {quiz.score} out of {quiz.question_number} correctly")
print()
print(f"Your total score is {quiz.score}. {remarks}")
print()
print()
print()

