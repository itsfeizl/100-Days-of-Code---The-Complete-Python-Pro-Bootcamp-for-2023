print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
bill = float(bill)

num_people = input("How many people to split the bill? ")
num_people = int(num_people)

tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_percentage = int(tip_percentage)

total_bill = bill + (bill * (tip_percentage/100))

bill_per_person = round(total_bill / num_people, 1)

print("Your total bill is " + str(total_bill) + ". Split among " + str(num_people) + ", each person should pay " + str(bill_per_person))