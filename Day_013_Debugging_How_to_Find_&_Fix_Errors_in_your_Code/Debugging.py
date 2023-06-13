############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   """The bug in this code is that at range(1, 20), i never reaches 20 as the range ends at 19. To debug the code, extend the range to 21."""
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# """The bug in this code is that the print statement specifies an index [dice_num] which goes beyond the number of items making up the dice_imgs list. To debug the code subtract 1 from the specified index [dice_num - 1] to bring it to the correct index of the last item in the list, which is 5.
# Alternatively, and even easier, you can just change the randint range to read from 0 to 5. That is dice_num = randint(0, 5)"""
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# """Here, the bug is that 1994 hasn't been referenced at all. The if statements specifies the years between 1980 and 1994 (not including 1994) whiles the elif statement specifies years greater than 1994. Thus, 1994 is completely ignored. Hence when the here 1994 is given as an input, nothing happens. To correct the code, the elif statement can specify years that are equal to or greater than 1994."""
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# """
# Here, firstly, the code block has wrong indentation. To correct the code, indent the print statement to fall within the if statement. 
# Secondly, input statements return strings. So to take numbers from input statement, inclose the input statement within an int() statement to convert the data type from string to integer.
# Finally, to use 'f' strings in python, specify 'f' at the beginning of the string. That is, print(f"You can drive at age {age}.")
# """
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# """
# If you print the word_per_page variable, it prints 0 which shows that the bug is in that part of the code. Upon investigation of that code (declaration of that variable), it becomes obvious that the wrong operator (==) is used instead of the assignment operator(=). Changing that fixes the code.
# """
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# """
# The bug in this code also stems from wrong indentation of code. Since the append statement is not within the for loop, only the last item after the mutation is appended to the second list. To correc the code, indent the append statement for it to fall within the for loop.
# """
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])