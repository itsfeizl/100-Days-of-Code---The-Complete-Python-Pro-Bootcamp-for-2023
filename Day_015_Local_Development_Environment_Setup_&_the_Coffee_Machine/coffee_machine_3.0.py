import os
clear = lambda: os.system('cls')


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}


resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def coffee_machine(customer_response):

    if customer_response == "espresso" or customer_response == "latte" or customer_response == "cappuccino":

        if customer_response == "espresso":
            MENU[customer_response]["ingredients"]["milk"] = 0

        if resources["water"] >= MENU[customer_response]["ingredients"]["water"]  and resources["coffee"] >= MENU[customer_response]["ingredients"]["coffee"] and resources["milk"] >= MENU[customer_response]["ingredients"]["milk"]:

            """If there is enough resources for an espresso, then the machine will ask for payment and process the order."""

            print("Please insert coins.")
            print()

            quarters = int(input("How many quarters? ")) * 0.25
            dimes = int(input("How many dimes? ")) * 0.10
            nickles = int(input("How many nickles? ")) * 0.05
            pennies = int(input("How many pennies? ")) * 0.01

            payment = quarters + dimes + nickles + pennies
            charge = MENU[customer_response]["cost"]

            if payment >= charge:
                resources["water"] = resources["water"] - MENU[customer_response]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[customer_response]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU[customer_response]["ingredients"]["milk"]
                resources["money"] += charge

                change = payment - charge
                clear()
                print(f"Here is your {customer_response}. ☕")
                print(f"And a ${change:.2f} change.")
                print("Thanks for buying from us. Enjoy.")
                
                print()
            elif payment < charge:
                clear()
                print(f"Sorry, ${payment:.2f} is not enough money. You need ${charge} for a {customer_response}.")
                print("Here's a refund of your payment.")
                print()
        else:
            if resources["water"] < MENU[customer_response]["ingredients"]["water"]:
                water_left = resources["water"]
                water_required = MENU[customer_response]["ingredients"]["water"] - resources["water"]
                print(f"Oops! There isn't enough water. At least {water_required} litres of water is required for a {customer_response}.")

                print()
                to_refill = input("Would you like to refill water? Type 'yes' or 'no': ").lower()
                print()

                if to_refill == "yes":
                    water_needed_to_fill_to_capacity = 300 - water_left
                    resources["water"] += water_needed_to_fill_to_capacity
                            
                else:
                    clear()
                    print("Money refunded.")
                    print()
                            
            elif resources["coffee"] < MENU[customer_response]["ingredients"]["coffee"]:
                coffee_left = resources["coffee"]
                coffee_required = MENU[customer_response]["ingredients"]["coffee"] - resources["coffee"]
                print(f"Oops! There isn't enough coffee. At least {coffee_required} litres of coffee is required for a {customer_response}.")

                print()
                to_refill = input("Would you like to refill coffee? Type 'yes' or 'no': ").lower()
                print()

                if to_refill == "yes":
                    coffee_needed_to_fill_to_capacity = 100 - coffee_left
                    resources["coffee"] += coffee_needed_to_fill_to_capacity
                            
                else:
                    clear()
                    print("Money refunded.")
                    print()

            elif resources["milk"] < MENU[customer_response]["ingredients"]["milk"]:
                milk_left = resources["milk"]
                milk_required = MENU[customer_response]["ingredients"]["milk"] - resources["milk"]
                print(f"Oops! There isn't enough milk. At least {milk_required} litres of milk is required for a {customer_response}.")

                print()
                to_refill = input("Would you like to refill milk? Type 'yes' or 'no': ").lower()
                print()

                if to_refill == "yes":
                    milk_needed_to_fill_to_capacity = 200 - milk_left
                    resources["milk"] += milk_needed_to_fill_to_capacity
                            
                else:
                    clear()
                    print("Money refunded.")
                    print()



at_coffee_machine = True

while at_coffee_machine:

    customer_response = input("What would you like? Espresso/Latte/Cappuccino/Report; or 'off' to power off machine: ").lower()
    print()

    if customer_response == "report":
        
        for key, value in resources.items():
            if key == "money":
                print(key.capitalize() + ": $" + str(value))
            else:
                print(key.capitalize() + ":", str(value) + "ml")
        print()
    

    coffee_machine(customer_response)

    if customer_response == "off":
            clear()
            print("Coffee machine powering down....")
            print("Coffee machine off.")
            at_coffee_machine = False