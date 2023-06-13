import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

no_error = True
while no_error:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        continue
    else:
        print(output_list)
        no_error = False


# Alternatively:
# def generate_phonetics():
#     word2 = input("Enter a word: ").upper()
#     try:
#         output_list2 = [phonetic_dict[letter] for letter in word2]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetics()
#     else:
#         print(output_list2)
#
#
# generate_phonetics()
