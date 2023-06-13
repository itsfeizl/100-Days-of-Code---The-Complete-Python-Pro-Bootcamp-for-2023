import random
import os
clear = lambda: os.system('cls')

word_list = ["aardvark", "baboon", "camel", "jealousy", "callous", "happy", "handsome", "righteous", "sizzling", "absurd", "insipid", "supercalifragilisticespialidocious", "hazardous", "milieu", "fulfilled", "friendly", "copacetic", "ascetic", "celibate", "diligent", "desirous", "facinating", "short-sightedness", "talented", "tentalizing", "titanium", "vivacious", "vigorous"]

randomWord = word_list[random.randint(0, (len(word_list) - 1))]


print("Let's play Hangwoman. Guess the letters in a word until you get the correct word.")
print()
print("Your mystery word has " + str(len(randomWord)) + " letters.")


mys_word = ""
for l in randomWord:
  l = "-"
  mys_word += l

print()
print()
print(mys_word)
print()
print()
  


list = list(mys_word)
wrong_letters = ""
final_word = ""

countdown = len(randomWord)
score_count = 0

while (final_word != randomWord) and (len(wrong_letters) < len(mys_word)):
  user_input = input("Guess a letter: ")
  clear()
  if user_input in randomWord:
    position = randomWord.index(user_input)
    ltr_occr = [pos for pos, char in enumerate(randomWord) if char == user_input]
    if user_input in final_word:
      print(f"You've already guessed the letter '{user_input}'")
    for i in ltr_occr:
      list[i] = user_input
    final_word = "".join(list)
    
    print()
    print(final_word)
    print()
    print()
    print()
    print()
        
  else:
    countdown -= 1
    print()
    print(f"Not quite. {countdown} lives left")
    print()
    print(final_word)
    print()
    print()
    wrong_letters += user_input
    if len(wrong_letters) == len(randomWord):
      print(f"You failed to predict the correct word: {randomWord} Game Over!")

print()
print()
score = 0
if final_word == randomWord:
  print(f"You win!")

