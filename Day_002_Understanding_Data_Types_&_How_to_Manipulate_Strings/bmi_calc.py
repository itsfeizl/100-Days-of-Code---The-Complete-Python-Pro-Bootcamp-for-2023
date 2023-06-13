print("Welcome to the BMI calculator. Find out what your Body Mass Index is by submitting your height and weight.")
print()

height = float(input("Enter your height: "))

weight = float(input("Enter your weight: "))

bmi = int(weight / (height * height))

print("Your BMI is " + str(bmi))