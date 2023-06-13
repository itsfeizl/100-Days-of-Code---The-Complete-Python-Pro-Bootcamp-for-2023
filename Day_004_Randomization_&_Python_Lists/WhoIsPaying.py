import random

names = input("Enter names of payers: ")
names_list = names.split(", ")


random_payer = names_list[random.randint(0, (len(names_list) - 1))]

print(f"Congratulations {random_payer}. You are our random payer today.")