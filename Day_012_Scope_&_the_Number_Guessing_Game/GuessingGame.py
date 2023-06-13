import random
logo = """  ________                                          
 /  _____/ __ __  ____   ______ ______ ____   ______
/   \  ___|  |  _/ __ \ /  ___//  ____/ __ \ /  ___/
\    \_\  |  |  \  ___/ \___ \ \___ \\  ___/ \___ \ 
 \______  |____/ \___  /____  /____  >\___  /____  >
        \/           \/     \/     \/     \/     \/ """


random_num = random.randint(1,100)

print(logo)
print()
print()
print("Welcome to Guesses, the Number Guessing Game!")

def difficulty_level():
    difficulty = input("Choose difficulty. Type 'easy', 'medium' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "medium":
        attempts = 7
    elif difficulty == "hard":
        attempts = 5

    return attempts

turns = difficulty_level()

print()
print("I'm thinking of a number between 1 and 100. What number is it?")
# print(f"Psss! The number is {random_num}")
print(f"You have {turns} attempts to find the number.")
print()

guess = int(input("Your guess: "))
print()

def check_answer(guess, random_num): 
      
  if guess < random_num:
    print("Too low.")
    print("Try again.") 
  elif guess > random_num:
    print("Too high.")
    print("Try again.") 

  if guess != random_num:
    global turns
    turns -= 1
    print(f"You have {turns} attempts remaining.")
    print()
    
    
while guess != random_num and turns > 0:
  check_answer(guess, random_num)
  if turns > 0:
    user_guess = int(input("Your guess: "))
    print()
    guess = user_guess
  else:
    print("You've run out of attempts. You lose!")

if guess == random_num:
  print(f"Wow! Your guess ({random_num}) is true. You win!")

