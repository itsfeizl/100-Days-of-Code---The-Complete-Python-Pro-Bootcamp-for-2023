MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

at_coffee_machine = True

while at_coffee_machine:

    customer_response = input("What would you like? (espresso/latte/cappuccino/report): ")

    if customer_response == "report":
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "ml")
        print("Money: $" + str(resources["money"]))

    elif customer_response == "espresso" or customer_response == "latte" or customer_response == "cappuccino":

        if resources["water"] == 0 or resources["milk"] == 0 or resources["coffee"] == 0:
            if resources["water"] == 0:
                print("Sorry. Not enough water. Turning machine off...")
                print("Machine is off.")
            elif resources["milk"] == 0:
                print("Sorry. Not enough milk. Turning machine off...")
                print("Machine is off.")
            elif resources["coffee"] == 0:
                print("Sorry. Not enough coffee. Turning machine off...")
                print("Machine is off.")

            at_coffee_machine = False

        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.10
            nickles = int(input("How many nickles? ")) * 0.05
            pennies = int(input("How many pennies? ")) * 0.01

            payment = quarters + dimes + nickles + pennies

            if customer_response == "espresso":
                if resources["water"] >= 50 and resources["coffee"] >= 18:
                    resources["water"] = resources["water"] - 50
                    resources["coffee"] = resources["coffee"] - 18
                    charge = 1.50
                    resources["money"] += charge
                    if payment > 1.50:
                        change = payment - charge
                        print(f"Here is ${change:.2f} change.")
                        print(f"Here is your {customer_response}. Enjoy.")
                    elif payment < 1.50:
                        print("Sorry, that's not enough money. Money refunded.")
                    else:
                        print("Here is your espresso. Enjoy.")
                else:
                    if resources["water"] < 50:
                        print("Oops! There isn't enough water. Sorry.")
                        print("Money refunded.")
                    elif resources["coffee"] < 18:
                        print("Oops! There isn't enough coffee. Sorry.")
                        print("Money refunded.")

            elif customer_response == "latte":
                if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
                    resources["water"] = resources["water"] - 200
                    resources["milk"] = resources["milk"] - 150
                    resources["coffee"] = resources["coffee"] - 24
                    charge = 2.50
                    resources["money"] += charge
                    if payment > 2.50:
                        change = payment - charge
                        print(f"Here is ${change:.2f} change.")
                        print(f"Here is your {customer_response}. Enjoy.")
                    elif payment < 2.50:
                        print("Sorry, that's not enough money. Money refunded.")
                    else:
                        print("Here is your espresso. Enjoy.")
                else:
                    if resources["water"] < 200:
                        print("Oops! There isn't enough water. Sorry.")
                        print("Money refunded.")
                    elif resources["milk"] < 150:
                        print("Oops! There isn't enough milk. Sorry.")
                        print("Money refunded.")
                    elif resources["coffee"] < 24:
                        print("Oops! There isn't enough coffee. Sorry.")
                        print("Money refunded.")
            elif customer_response == "cappuccino":
                if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
                    resources["water"] = resources["water"] - 250
                    resources["milk"] = resources["milk"] - 100
                    resources["coffee"] = resources["coffee"] - 24
                    charge = 3.00
                    resources["money"] += charge
                    if payment > 3.00:
                        change = payment - charge
                        print(f"Here is ${change:.2f} change.")
                        print(f"Here is your {customer_response}. Enjoy.")
                    elif payment < 3.00:
                        print("Sorry, that's not enough money. Money refunded.")
                    else:
                        print("Here is your espresso. Enjoy.")
                else:
                    if resources["water"] < 250:
                        print("Oops! There isn't enough water. Sorry.")
                        print("Money refunded.")
                    elif resources["milk"] < 100:
                        print("Oops! There isn't enough milk. Sorry.")
                        print("Money refunded.")
                    elif resources["coffee"] < 24:
                        print("Oops! There isn't enough coffee. Sorry.")
                        print("Money refunded.")

    elif customer_response == "off":
        at_coffee_machine = False
