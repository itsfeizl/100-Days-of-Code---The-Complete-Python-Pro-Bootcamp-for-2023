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


def coffee_machine(customer_response):
    
    
    if customer_response == "report":
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "ml")
        print("Money: $" + str(resources["money"]))

    elif customer_response == "espresso" or customer_response == "latte" or customer_response == "cappuccino":

        

        if MENU[customer_response]["ingredients"] == "milk":

            if resources["water"] >= MENU[customer_response]["ingredients"]["water"]  and resources["coffee"] >= MENU[customer_response]["ingredients"]["coffee"] and resources["milk"] >= MENU[customer_response]["ingredients"]["milk"]:
                    
                """If there is enough resources for an espresso, then the machine will ask for payment and process the order."""

                print("Please insert coins.")
                quarters = int(input("How many quarters? ")) * 0.25
                dimes = int(input("How many dimes? ")) * 0.10
                nickles = int(input("How many nickles? ")) * 0.05
                pennies = int(input("How many pennies? ")) * 0.01

                payment = quarters + dimes + nickles + pennies

                resources["water"] = resources["water"] - MENU[customer_response]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[customer_response]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU[customer_response]["ingredients"]["milk"]
                charge = MENU[customer_response]["cost"]
                resources["money"] += charge

                if payment > charge:
                    change = payment - charge
                    print(f"Here is ${change:.2f} change.")
                    print(f"Here is your {customer_response}. Enjoy.")
                elif payment < charge:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    print("Here is your espresso. Enjoy.")
            else:
                if resources["water"] < MENU[customer_response]["ingredients"]["water"]:
                    water_left = resources["water"]
                    water_required = MENU[customer_response]["ingredients"]["water"] - resources["water"]
                    print(f"Oops! There isn't enough water. At least {water_required} litres of water is required for a {customer_response}.")

                    to_refill = input("Would you like to refill water? ").lower()

                    if to_refill == "yes":
                        refill = input("Refill with minimum required or to capacity? Type 'min' or 'max': ").lower()
                        if refill == "min":
                            resources["water"] += water_required
                        elif refill == "max":
                            water_needed_to_fill_to_capacity = 300 - water_left
                            resources["water"] += water_needed_to_fill_to_capacity
                        
                    else:
                        print("Money refunded.")
                        print("Coffee machine powering down....")
                        print("Coffee machine off.")
                        
                elif resources["coffee"] < MENU[customer_response]["ingredients"]["coffee"]:
                    coffee_left = resources["coffee"]
                    coffee_required = MENU[customer_response]["ingredients"]["coffee"] - resources["coffee"]
                    print(f"Oops! There isn't enough coffee. At least {coffee_required} litres of coffee is required for a {customer_response}.")

                    to_refill = input("Would you like to refill coffee? ").lower()

                    if to_refill == "yes":
                        refill = input("Refill with minimum required or to capacity? Type 'min' or 'max': ").lower()
                        if refill == "min":
                            resources["coffee"] += coffee_required
                        elif refill == "max":
                            coffee_needed_to_fill_to_capacity = 100 - coffee_left
                            resources["coffee"] += coffee_needed_to_fill_to_capacity
                        
                    else:
                        print("Money refunded.")
                        print("Coffee machine powering down....")
                        print("Coffee machine off.")

                elif resources["milk"] < MENU[customer_response]["ingredients"]["milk"]:
                    milk_left = resources["milk"]
                    milk_required = MENU[customer_response]["ingredients"]["milk"] - resources["milk"]
                    print(f"Oops! There isn't enough milk. At least {milk_required} litres of milk is required for a {customer_response}.")

                    to_refill = input("Would you like to refill milk? ").lower()

                    if to_refill == "yes":
                        refill = input("Refill with minimum required or to capacity? Type 'min' or 'max': ").lower()
                        if refill == "min":
                            resources["milk"] += milk_required
                        elif refill == "max":
                            milk_needed_to_fill_to_capacity = 200 - milk_left
                            resources["milk"] += milk_needed_to_fill_to_capacity
                        
                    else:
                        print("Money refunded.")
                        print("Coffee machine powering down....")
                        print("Coffee machine off.")

        else:
            if resources["water"] >= MENU[customer_response]["ingredients"]["water"] and resources["coffee"] >= MENU[customer_response]["ingredients"]["coffee"]:
                print("Please insert coins.")
                quarters = int(input("How many quarters? ")) * 0.25
                dimes = int(input("How many dimes? ")) * 0.10
                nickles = int(input("How many nickles? ")) * 0.05
                pennies = int(input("How many pennies? ")) * 0.01

                payment = quarters + dimes + nickles + pennies

                resources["water"] = resources["water"] - MENU[customer_response]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[customer_response]["ingredients"]["coffee"]
                charge = MENU[customer_response]["cost"]
                resources["money"] += charge

                if payment > charge:
                    change = payment - charge
                    print(f"Here is ${change:.2f} change.")
                    print(f"Here is your {customer_response}. Enjoy.")
                elif payment < charge:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    print("Here is your espresso. Enjoy.")
            else:
                if resources["water"] < MENU[customer_response]["ingredients"]["water"]:
                    water_left = resources["water"]
                    water_required = MENU[customer_response]["ingredients"]["water"] - resources["water"]
                    print(f"Oops! There isn't enough water. At least {water_required} litres of water is required for a {customer_response}.")

                    to_refill = input("Would you like to refill water? ").lower()

                    if to_refill == "yes":
                        refill = input("Refill with minimum required or to capacity? Type 'min' or 'max': ").lower()
                        if refill == "min":
                            resources["water"] += water_required
                        elif refill == "max":
                            water_needed_to_fill_to_capacity = 300 - water_left
                            resources["water"] += water_needed_to_fill_to_capacity
                        
                    else:
                        print("Money refunded.")
                        print("Coffee machine powering down....")
                        print("Coffee machine off.")
            
                elif resources["coffee"] < MENU[customer_response]["ingredients"]["coffee"]:
                    coffee_left = resources["coffee"]
                    coffee_required = MENU[customer_response]["ingredients"]["coffee"] - resources["coffee"]
                    print(f"Oops! There isn't enough coffee. At least {coffee_required} litres of coffee is required for a {customer_response}.")

                    to_refill = input("Would you like to refill coffee? ").lower()

                    if to_refill == "yes":
                        refill = input("Refill with minimum required or to capacity? Type 'min' or 'max': ").lower()
                        if refill == "min":
                            resources["coffee"] += coffee_required
                        elif refill == "max":
                            coffee_needed_to_fill_to_capacity = 100 - coffee_left
                            resources["coffee"] += coffee_needed_to_fill_to_capacity
                        
                    else:
                        print("Money refunded.")
                        print("Coffee machine powering down....")
                        print("Coffee machine off.")


at_coffee_machine = True


while at_coffee_machine:

    customer_response = input("What would you like? (espresso/latte/cappuccino/report): ")
    if customer_response == "off":
        at_coffee_machine = False
    else:
        coffee_machine(customer_response)


