alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

def encrypt(text, shift):
    encoded_text = ""
    for letter in text:
        if letter in alphabet:
            index_of_letter = alphabet.index(letter)
            if index_of_letter <= ((len(alphabet)-1) - shift):
                new_index = index_of_letter + shift
                letter = alphabet[new_index]
                encoded_text += letter
            else:
                new_index = (index_of_letter + shift) - (len(alphabet))
                letter = alphabet[new_index]
                encoded_text += letter
    print()     
    print(f"The encoded text is... {encoded_text}")
    print()  


def decrypt(text, shift):
    decoded_text = ""
    for letter in text:
        if letter in alphabet:
            index_of_letter = alphabet.index(letter)
            new_index = index_of_letter - shift
            letter = alphabet[new_index]
            decoded_text += letter
    print()    
    print(f"The decoded text is... {decoded_text}")
    print()  






def cypher_encryption():
  
    text = input("Type your message:\n")
    print()
    shift = int(input("Type the shift number:\n"))
    print()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    print()

    if direction == "encode":
        encrypt(text, shift)

    elif direction == "decode":
        decrypt(text, shift)

    else:
        user_input = input("Please enter 'encode' or 'decode':\n")
        if user_input == "encode":
            encrypt(text, shift)
        else:
            decrypt(text, shift)
    

cypher_encryption()

go_again = input("Would you like to go again? Type 'yes' or 'no':\n")
if go_again == "yes":
    print()
    cypher_encryption()