# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
div_by_4 = year % 4
div_by_100 = year % 100
div_by_400 = year % 400

if div_by_4 == 0:
  if div_by_100 == 0:
    if div_by_400 == 0:
      print("Leap year.")
    else: print("Not leap year.")
  else: print("Leap year.")
else: print("Not leap year.")