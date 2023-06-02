# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Extract letter text into a variable
with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()

# Create list from names of invited
with open("./Input/Names/invited_names.txt", "r") as names:
    names_list = names.read().split("\n")

# Create letter for each invited replacing placeholder with their names
for name in names_list:
    corrected_letter = letter.replace("[name]", name)
    with open("../Mail_Merge_Project/Output/ReadyToSend/Letter_for_" + name + ".txt", mode="w") as file:
        file.write(corrected_letter)
