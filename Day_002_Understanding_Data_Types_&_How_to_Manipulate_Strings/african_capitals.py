play_game = input("How much do you know about Africa? This game tests you on this knowledge by asking you to name the capital cities of some African coutries. Each correct answer you get is worth 2 points. But you have just one shot for a wrong answer takes you out of the game. Are you ready to play? Type 'Y' or 'N':\n").lower()

score = 0

if play_game == "y":
  print()
  capital_algeria = input("What is the capital of ALGERIA? 'Algiers' or 'Gaborone':\n").lower()
  if capital_algeria == "algiers":
    score += 2
    print()
    print(f"Correct! Your score is {score}")
    print()
    capital_ghana = input("What is the capital of Ghana? Is it 'Lome' or 'Accra'?\n").lower()
    if capital_ghana == "accra":
      score += 2
      print()
      print(f"Excellent! Your score is {score}")
      print()
      capital_morocco = input("What is the capital of Morocco? Is it 'Marakesh' or 'Rabat'?\n").lower()
      if capital_morocco == "rabat":
        score += 2
        print()
        print(f"Excellent! Your score is {score}")
        print()
        capital_nigeria = input("What is the capital of Nigeria? Is it 'Lagos' or 'Abuja'? \n").lower()
        if capital_nigeria == "abuja":
          score += 2
          print()
          print(f"Excellent! Your score is {score}")
          print()

          capital_ethiopia = input("What is the capital of Ethiopia? Is it 'Antanarivo' or 'Adis Ababa?'\n").lower()
          if capital_ethiopia == "adis ababa":
            score +=2
            print()
            print(f"Great! Your score is {score}")
            print()

            capital_madagascar = input("For double of your current score tally, what is the capital of Madagascar? Sorry, no options to choose from. \n").lower()
            if capital_madagascar == "antananarivo":
              score *=2
              print()
              print(f"Wow! Excellent job! You answered correctly to earn a grand total of {score} points. Congratulations.")
          else:
            print(f"Oops! The correct answer is 'Adis Ababa'. You lost with a score tally of {score}")
        else:
          print(f"Sorry. The correct answer is Abuja. You lost with a score of {score}")
      else:
        print()
        print(f"Sorry. The correct answer is Rabat. You lost with a score of {score}")
    else:
      print()
      print(f"Sorry. The correct answer is Accra. You lost with a score of {score}")
  else:
    print()
    print(f"Sorry. The correct answer is Algiers. You lost with a score of {score}")
else:
  print("Next time, I guess.")