from data import general_knowledge_data, history_data, geography_data
from question_model import Question
from quiz_brain import QuizBrain
import random


general_knowledge_qtn_list = random.sample(general_knowledge_data, 10)
geography_qtn_list = random.sample(geography_data, 10)
history_qtn_list = random.sample(history_data, 10)


print()
category = input("Welcome to the Quiz Game. Choose category (General Knowledge/History/Geography): ").lower()

if category == "general knowledge":
    question_data = general_knowledge_qtn_list
elif category == "history":
    question_data = history_qtn_list
elif category == "geography":
    question_data = geography_qtn_list



question_bank = []

for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

print()
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"You've answered {quiz.score} out of {quiz.question_number} correctly")
print(f"Total score: {quiz.score}")
print()