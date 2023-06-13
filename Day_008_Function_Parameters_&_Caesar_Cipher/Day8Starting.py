# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Greetings!")
  print("My name is Feizl")
  print("Welcome to my world.")

# greet()



user_name = input("What's your name? ")
user_location = input("What's your location? ")

def greet_with_name(name, location):
  print(f"Hello {user_name} from {user_location}!")
  print("My name is Feizl")
  print("It's really nice to meet you.")

greet_with_name(user_name, user_location)