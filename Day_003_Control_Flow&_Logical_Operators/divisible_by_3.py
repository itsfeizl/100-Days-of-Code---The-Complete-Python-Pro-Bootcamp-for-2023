num = input("Enter a number to find out whether the number is divisible by 3: \n")
print()



curr_str = ""
for item in num:
    curr_str += item

if int(curr_str) % 3 == 0:
  print("Your number is divisible by 3.")
else:
  print("Your number is not divisible by 3.")