import time
from threading import Thread

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

correct_answer = ["c", "d", "a", "b"]

print()
print("Welcome to 'Who Wants to be a Millionair?' To play, answer this question correctly.")
print("You have 30 seconds.")
print()



within_time = True #declare boolean so that code can be executed only if it is still True
t1 = time.time()

qualifier_qtn = input("Put the following races in order according to their lengths, from the shortest to the longest: \nA. Iditarod Dog Sled Race\nB. Tour De France\nC. London Marathon\nD. Indianapolis 500\n\nEnter answer (option letters) without spacing: ").lower() 
print()



t2 = time.time()
t = round(t2 - t1, 2)
if t > 20:
    print(f"Time spent: {t} seconds.")
    print("You failed to answer in time.")
    print()
    print("Sorry, you do not qualify for the 'Hot Seat'.")
    print()
    within_time = False

else:
    print(f"Time spent: {t} seconds.")
    print("You answered just in time.")
    player_input = list(qualifier_qtn)
    if player_input == correct_answer:
        
        print("Your answer is in the correct order: C-D-A-B")
        print()
        print("Congratulations! You've qualified for the 'Hot Seat'.")
        print()
        print()
    
    else:
        print("You've failed to answer in the correct order: C-D-A-B")
        print()
        print("Sorry, you do not qualify for the 'Hot Seat'.")
        print()
        print()



# question_bank = []

# for item in question_data:
#     question = Question(item["text"], item["answer"])
#     question_bank.append(question)

# quiz = QuizBrain(question_bank)

# print()
# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz.")
# print(f"You've answered {quiz.score} out of {quiz.question_number} correctly")
# print(f"Total score: {quiz.score}")
# print()