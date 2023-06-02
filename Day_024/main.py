# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("../../my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nI just can't wait to be a Python programmer.")

with open("newest_file.txt", mode="w") as file:
    file.write("This is some new text.")

# with open("a_file.txt", mode="a") as file:
#     file.write("This is some new text.")
