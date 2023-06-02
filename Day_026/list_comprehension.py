# List Comprehension
# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [num * 2 for num in numbers]
print(new_numbers)
print()

name = "Faisal"
letters_in_faisal = [letter for letter in name]
print(letters_in_faisal)

doubled_nums = [num * 2 for num in range(1, 5)]
print(doubled_nums)
print()


# Conditional List Comprehension
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]
four_letter_names = [name for name in names if len(name) == 4]
print(four_letter_names)
print()

uppercase_names_list = [name.upper() for name in names if len(name) > 4]
print(uppercase_names_list)
print()

st_names = ["Alex", "Beth", "Caroline", "Aaron", "Dave", "Eleanor", "Freddy", "Abigail"]
names_starting_with_a = [name for name in st_names if name[0] == "A"]
print(names_starting_with_a)
print()


# Challenge 1: Squared numbers test
# Create a new list of numbers that is made up of each
# of the numbers in the numbers list squared

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]


# Challenge 2: Filtering even numbers
# You are going to write a List Comprehension to
# create a new list called result. This new list
# should only contain the even numbers from the
# list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)


# Challenge 3
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers,
# each number on a new line.
# You are going to create a list called result which contains the numbers that are
# common in both files.

with open("file1.txt") as file1:
    contents = file1.read()
    list_1 = contents.split("\n")
    print(list_1)

with open("file2.txt") as file2:
    contents = file2.read()
    list_2 = contents.split("\n")

result = [int(num) for num in list_1 if num in list_2 and num != ""]

print(result)
