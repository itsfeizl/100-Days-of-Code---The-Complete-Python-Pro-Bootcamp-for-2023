import os
clear = lambda: os.system('cls')

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

menu_dic = MENU


pos = list((menu_dic["espresso"]["ingredients"]).keys()).index('coffee')
items = list((menu_dic["espresso"]["ingredients"]).items())
items.insert(pos, ('milk', 0))
(menu_dic["espresso"]["ingredients"]) = dict(items)

resources = {"water": 500, "milk": 200, "coffee": 100}
resources_original_level = {}
for item, value in resources.items():
    resources_original_level[item] = value
money = 0


def check_resource_sufficiency():
    """Function checks if resources available is sufficient to process order and return True"""

    global ingredients_dict
    ingredients_dict = menu_dic[customer_order]["ingredients"]
    for item in ingredients_dict:
        if resources[item] >= ingredients_dict[item]:
            return True
        else:
            if resources[item] == 0:
                clear()
                print(f"Sorry, can't process your order because {item} container is empty.")
                print()
            else:
                print(f"{item.capitalize()} level is insufficient for a {customer_order}")
                print("Try our other refereshing beverages:")
                for key, value in menu_dic.items():
                    if key != customer_order:
                        prices = menu_dic[key]["cost"]
                        print(f"{key.capitalize()} : ${prices:.2f}")
                print()
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


        for item, value in resources.items():

            if item == "money":
                    continue
            

            for key, value in menu_dic.items():
                order_ingredient_level = menu_dic[key]["ingredients"][item]


            if resources[item] > 0 and resources[item] < order_ingredient_level:
                print(f"{item.capitalize()} level ({resources[item]}) is low. A refill may be needed.")
                refill_container = input(f"Refill {item} container? Enter 'YES' or 'NO': ").lower()
                print()

                if refill_container == "yes":
                    resources[item] += resources_original_level[item] - resources[item]
                    print(f"{item.capitalize()} level now at {resources_original_level[item]}")
                else:
                    clear()

            elif resources[item] == 0:
                print(f"{item.capitalize()} is empty. Machine can't operate with {item} level at {resources[item]}.")
                refill_container = input(f"Refill {item} container? Enter 'YES' or 'NO': ").lower()
                print()

                if refill_container == "yes":
                    resources[item] += resources_original_level[item]
                    print(f"{item.capitalize()} level now at {resources_original_level[item]}")
                
                elif refill_container == "no":
                    clear()


    elif customer_order == "espresso" or customer_order == "latte" or customer_order == "cappuccino":
        # Check if available resources are sufficient for customer order
        if check_resource_sufficiency():
            # Confirm order, announce price
            order_price = menu_dic[customer_order]["cost"]
            print(f"Your order: {customer_order.capitalize()}.")
            print(f"Price: ${order_price:.2f}.")
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
                    if payment >= menu_dic[customer_order]["cost"]:
                        
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
                            resources[item] -= menu_dic[customer_order]["ingredients"][item]

                        continue_ordering = input("Would you like to put in another order? Enter 'YES' or 'NO': ").lower()
                        print()

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
                            payment += payment
                        else:
                            load_more_coins = False

            elif proceed == "change": 
                continue    

            else:
                # Restart the coffee machine if customer wants to change order or doesn't want to continue with order.
                clear() 
                continue
            
            
    # Type 'off' to exit the while loop (Turn off the coffee machine)        
    elif customer_order == "off":
        clear()
        coffee_machine_on = False