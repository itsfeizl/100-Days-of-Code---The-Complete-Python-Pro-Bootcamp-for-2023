print("Are you crushing on somebody? Try the 'Love Calculator' to find out what your chances with them.")

user_name = input("What is your name? \n").lower()
crush_name = input("What is their name? \n")

count_T = user_name.count("t") + crush_name.count("t")
count_R = user_name.count("r") + crush_name.count("r")
count_U = user_name.count("u") + crush_name.count("u")
count_E = user_name.count("e") + crush_name.count("e")

count_L = user_name.count("l") + crush_name.count("l")
count_O = user_name.count("o") + crush_name.count("o")
count_V = user_name.count("v") + crush_name.count("v")
count_E = user_name.count("e") + crush_name.count("e")



total_count_true = str(count_T + count_R + count_U + count_E)
total_count_love = str(count_L + count_O + count_V + count_E)

love_percentage = int(total_count_true + total_count_love)

print(love_percentage)

if love_percentage < 10 or love_percentage > 90:
  print(f"Your score is {love_percentage}.  You two will go together like coke and mentos.")
elif love_percentage > 40 and love_percentage < 50:
  print(f"Your score is {love_percentage}. You're alright together.")
else:
  print(f"Your score is {love_percentage}")