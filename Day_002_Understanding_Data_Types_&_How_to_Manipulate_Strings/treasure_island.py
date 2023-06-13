print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

option_left = input(
  "You're at a cross road. Where do you want to go? Type 'Left' or 'Right': \n"
).lower()

print()

if option_left == "left":
  option_wait = input(
    "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n"
  ).lower()
  print()
  if option_wait == "wait":
    door_option = input(
      "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
    ).lower()
    print()
    if door_option == "yellow":
      print()
      print("You win!")
    elif door_option == "blue" or door_option == "red":
      print()
      print("You lose!")
    else:
      print()
      print("Type 'Red', 'Yellow' or 'Blue'! \nTry again.")
  elif option_wait == "swim":
    print()
    print("You get attacked by an angry trout. \nGame Over.")
  else:
    print("Type 'Wait' or 'Swim'! \nTry again.")
else:
  if option_left == "right":
    print()
    print("You fell into a ditch. \nGame over. \nBetter luck next time.")
  else:
    print()
    print("Type 'Left' or 'Right'! \nTry again.")
