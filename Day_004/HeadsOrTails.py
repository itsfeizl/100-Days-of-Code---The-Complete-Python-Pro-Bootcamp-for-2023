import random

user_input = input("Heads or Tails? \n").lower()

random_num = random.randint(0, 1)

toss = ""
if random_num == 1:
  toss = "heads"
  print("It's Heads")
else:
  toss = "tails"
  print("It's tails")

if user_input == toss:
  print("You win!")
else:
  print("You lose.")