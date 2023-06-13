print("Suppose you'll live to be 90. Are you interested in how many weeks you have left to live? Input your age and find out:")

print()
print()

year_in_days = 365
year_in_weeks = 52
year_in_months = 12

ninety_years_in_days = 90 * 365
ninety_years_in_weeks = 90 * 52
ninety_years_in_months = 90 * 12

user_age = int(input("Enter your age:"))
user_age_in_days = user_age * year_in_days
user_age_in_weeks = user_age * year_in_weeks
user_age_in_months = user_age * year_in_months

user_years_left_in_days = ninety_years_in_days - user_age_in_days
user_years_left_in_weeks = ninety_years_in_weeks - user_age_in_weeks
user_years_left_in_months = ninety_years_in_months - user_age_in_months
user_years_left_in_years = 90 - user_age

print()
print()

print("If you'll live to be 90, and you're now " + str(user_age) + " old, then you have: \n" + str(user_years_left_in_years) + " years, or \n" + str(user_years_left_in_months) + " months, or \n" + str(user_years_left_in_weeks) + " weeks, or \n" + str(user_years_left_in_days) + " days to live.")