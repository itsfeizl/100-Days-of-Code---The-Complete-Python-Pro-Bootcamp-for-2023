alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(direction, text, shift):
  cypher_text = ""
  for letter in text:
    index_of_letter = alphabet.index(letter)
    if direction == "encode":
      cypher_text += alphabet[index_of_letter + shift]
    else:
      cypher_text += alphabet[index_of_letter - shift]
  print(f"The {direction}d text is {cypher_text}")

#Alternatively:

# def caesar(direction, text, shift):
#   cypher_text = ""
#   if direction == "decode":
#       shift *= -1
#   for letter in text:
#     index_of_letter = alphabet.index(letter)
#     cypher_text += alphabet[index_of_letter + shift]
    
#   print(f"The {direction}d text is {cypher_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(direction, text, shift)
