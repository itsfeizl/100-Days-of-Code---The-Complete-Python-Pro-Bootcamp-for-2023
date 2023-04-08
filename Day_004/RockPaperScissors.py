rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

options = [rock, paper, scissors]

random_num = random.randint(1, 3)
computer_choice = options[random_num - 1]

user_choice = input("Rock, Paper, or Scissors? \n").lower()
print()
print()
print()

if user_choice == "rock":
  user_choice = rock
elif user_choice == "paper":
  user_choice = paper
else:
  user_choice = scissors
  
if computer_choice == rock:
  if user_choice == rock:
    print(f"Computer {computer_choice}")
    print(f"User: {user_choice}")
    print("It's a draw.")
  elif user_choice == paper:
    print(f"Computer {computer_choice}")
    print(f"User: {user_choice}")
    print("Paper covers rock; You Win!")
  else:
    print(f"Computer {computer_choice}")
    print(f"User: {user_choice}")
    print("Rock crushes scissors. You lose!")
elif computer_choice == paper:
  if user_choice == rock:
    print(f"Computer {computer_choice}")
    print(f"User: {user_choice}")
    print("Paper covers rock; You win!")
  elif user_choice == paper:
    print(f"Computer {computer_choice}")
    print(f"User: {user_choice}")
    print("It's a draw.")
  else:
    print(f"Computer {computer_choice}")
    print(f"User: {user_choice}")
    print("Scissors cut paper. You win!")
else:
  if user_choice == rock:
    print(f"Computer {computer_choice}")
    print(f"User: {user_choice}")
    print("Rock crushes scissors; You win!")
  elif user_choice == paper:
    print(f"Computer {computer_choice}")
    print(f"User: {user_choice}")
    print("Scissors cut paper. You lose!")
  else:
    print(f"Computer {computer_choice}")
    print(f"User: {user_choice}")
    print("It's a draw.")
