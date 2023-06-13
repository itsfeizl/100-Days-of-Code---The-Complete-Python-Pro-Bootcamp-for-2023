# Exceptions
# try: (Something that might cause an exception)
# except: (Do this if there was an exception)
# else: (Do this if there were no exceptions)
# finally: (Do this no matter what happens)

# FileNotFound

# try:
#     file = open("a_file.txt")
    # a_file.txt doesn't exist so an error (FileNotFoundError) will be thrown
    # which should be caught in the except clause

    # a_dictionary = {"key": "value"}
    # print(a_dictionary["item"])
    # The print statement will throw an error (keyError) because a_dictionary doesn't
    # have a key with the name item. This error will also be caught in the except clause
    # specified for it.

    # different except clauses must be defined for different expected errors since one
    # except clause will except all errors after the first one

# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something...")
#
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
#
# else:
#     content = file.read()
#     print(content)

# finally:
#     file.close()
#     print("file was closed.")
#     raise TypeError("This is an error that I made up.")


# Raise your own except

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height cannot be over 3 meters.")

else:
    bmi = weight / height ** 2
    print(bmi)
