import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_alphabets_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What is your name? ").upper().replace(" ", "")
output_list = [phonetic_alphabets_dict[letter] for letter in user_input]
print(output_list)
