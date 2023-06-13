#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator! We help you generate a strong password for use. Set up your password by answering the follow:")
print()
nr_letters= int(input("1 - How many letters would you like in your password? ")) 
nr_symbols = int(input("2 - How many symbols would you like? "))
nr_numbers = int(input("3 - How many numbers would you like? "))
print()
print()

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_letters = ""
random_numbers = ""
random_symbols = ""

for letter in letters:
  if len(random_letters) < nr_letters:
    random_letters += letters[random.randint(0, len(letters) - 1)]

for symbol in symbols:
  if len(random_symbols) < nr_symbols:
    random_symbols += symbols[random.randint(0, len(symbols) - 1)]

for number in numbers:
  if len(random_numbers) < nr_numbers:
    random_numbers += numbers[random.randint(0, len(numbers) - 1)]

random_chars = random_letters + random_symbols + random_numbers
 

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_chars_list = list(random_chars)
random.shuffle(random_chars_list)
password = ''.join(random_chars_list)
print(f"Your new super strong password is: {password}")