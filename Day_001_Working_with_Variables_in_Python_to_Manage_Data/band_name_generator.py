#1. Create a greeting for your program.
print("Welcome to the band-name generator app which helps you to come up with awesome names for your band. Lets get started:")
print()

#2. Ask the user for the city that they grew up in.
city = input("What city are you from? \n")
print()

#3. Ask the user for the name of a pet.
pet = input("What's your pet's name? \n")
print()

#4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet
print(f"A cool name for your band could be the {band_name}")

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end