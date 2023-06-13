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


resources = {"water": 300, "milk": 200, "coffee": 100}
money = 0


def check_resource_sufficiency():
    """Function checks if resources available is sufficient to process order and return True"""
    global ingredients_dict
    ingredients_dict = MENU[customer_order]["ingredients"]
    for item in ingredients_dict:
        if resources[item] >= ingredients_dict[item]:
            return True
        else:
            return False

def process_coins():
    """Function process coins paid into machine and returns total"""

    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01

    total_coins = quarters + dimes + nickles + pennies
    return total_coins




coffee_machine_on = True

while coffee_machine_on:

    # Ask customer to place their order
    # Vendor can enter 'Report' to check whether available resources in order to decided whether to replenish resources 
    # Vendor can also enter 'OFF' to turn off the machine
    customer_order = input("What would you like? Espresso/Latte/Cappuccino/Report: ").lower()
    print()

    # Print report
    if customer_order == "report":
        for item, value in resources.items():
            print(item.capitalize() + ":", str(value) + "ml")
        print(f"Money: ${money:.2f}")
        print()


    elif customer_order == "espresso" or customer_order == "latte" or customer_order == "cappuccino":
        # Check if available resources are sufficient for customer order
        if check_resource_sufficiency():
            # Confirm order, announce price
            order_price = MENU[customer_order]["cost"]
            print(f"You've ordered a/an {customer_order.capitalize()}.")
            print(f"Order price is ${order_price:.2f}.")
            print()

            # Ask if customer wants to proceed with order or change it
            print("Would you like to proceed?")
            proceed = input("Enter 'YES' or 'NO'; or 'CHANGE' to change your order. ").lower()
            print()
            if proceed == "yes":
                # Customer wants to proceed with order. Ask for payment
                print("Load coins: ")
                print()
                payment = process_coins()
                print()

                # While loop to revert to checking payment if customer loads more coins due to initial coins loaded being insufficient
                load_more_coins = True
                while load_more_coins:
                    # Check if payment is sufficient against order price and process order
                    if payment >= MENU[customer_order]["cost"]:
                        
                        # Loop ends after coins reloaded is sufficient to continue to transaction
                        load_more_coins = False

                        change = round(payment - order_price, 2)
                        money += order_price
                        clear()
                        print(f"Here's your {customer_order}.")
                        print(f"And a ${change} change.")
                        print("Enjoy.")
                        print()

                        # Once order is processed, deduct resources used in processing order from the resources container(dictionary)
                        for item, value in resources.items():
                            # Espresso isn't processed with milk, so set the value of milk in espresso to 0
                            if customer_order == "espresso":
                                MENU[customer_order]["ingredients"]["milk"] = 0
                                resources[item] -= MENU[customer_order]["ingredients"][item]
                            else:
                                resources[item] -= MENU[customer_order]["ingredients"][item]

                        continue_ordering = input("Would you like to put in another order? Enter 'YES' or 'NO': ").lower()

                        if continue_ordering == "yes":
                            continue
                        else:
                            clear()
                            continue
                        
                    else:
                        clear()
                        # Declare insufficiency of funds
                        print(f"Insufficient funds.")
                        print(f"Order cost is ${order_price:.2f} for a/an {customer_order.capitalize()} but you've paid only ${payment}")
                        print()
                        # Ask whether customer will load more coins
                        more_coins = input("Would you like load more coins? Enter 'YES' or 'NO': ")
                        print()
                        if more_coins == "yes":
                            # Allow customer to load more coins if they answered yes
                            payment = process_coins()
                        else:
                            load_more_coins = False

            elif proceed == "change": 
                continue    

            else:
                # Restart the coffee machine if customer wants to change order or doesn't want to continue with order.
                clear() 
                continue

        else:
            clear()
            # Declare insufficiency of resources for customer order
            print(f"There isn't sufficient resources for a/an {customer_order.capitalize()}.")
            print()

            # Suggesting other orders on the menu
            print("Try our other refereshing beverages:")
            for key, value in MENU.items():
                if key != customer_order:
                    prices = MENU[key]["cost"]
                    print(f"{key.capitalize()} : ${prices:.2f}")
            print()
            
            
    # Type 'off' to exit the while loop (Turn off the coffee machine)        
    elif customer_order == "off":
        clear()
        coffee_machine_on = False