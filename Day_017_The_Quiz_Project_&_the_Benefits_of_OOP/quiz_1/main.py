from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

print()
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"You've answered {quiz.score} out of {quiz.question_number} correctly")
print(f"Total score: {quiz.score}")
print()