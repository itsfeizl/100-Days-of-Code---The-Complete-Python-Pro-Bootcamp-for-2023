from data import MENU, resources

money = 0

def get_drinks():
    for item, value in MENU.items():
        drink = item 
    return drink

drink = get_drinks()

def get_available_resources(resources):
    for item, value in resources.items():
        resource_available = item
    return resource_available
resource_available = get_available_resources(resources)



def check_resource_sufficiency(resources):

    global ingredients_list 
    ingredients_list = MENU[drink]["ingredients"]         

    for item, value in ingredients_list.items():
        value_of_required_ingredient = value
        
    for item, value in resources.items():
        if value > value_of_required_ingredient:
            return True
        else:
            return False

resource_sufficient = check_resource_sufficiency(resources)

def process_coins():
    print("Please insert coins.")
    print()

    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01

    total_coins = quarters + dimes + nickles + pennies
    return total_coins
 




coffee_machine_on = True

while coffee_machine_on:

    customer_response = input("What would you like? Espresso/Latte/Cappuccino/Report: ").lower()
    print()

    if customer_response == "report":

        for item, value in resources.items():
            print(item + ":", str(value) + "ml")
        print(f"Money: ${money}")
        print()


    elif customer_response == "espresso" or customer_response == "latte" or customer_response == "cappuccino": 
        
        if resource_sufficient:

            payment = process_coins()
            print()

            if payment >= MENU[customer_response]["cost"]:

                drink_cost = MENU[customer_response]["cost"]
                change = round(payment - drink_cost, 2)
                money += drink_cost
                print(f"Here's your {customer_response}.")
                print(f"And a ${change} change.")
                print("Enjoy.")
                print()

                for item, value in ingredients_list.items():
                    ingredient_qty = value
                    for item, value in resources.items():
                        resource_quantity = value
            
                        resource_quantity - ingredient_qty

            else:
                print(f"Insufficient funds for a {customer_response}.")
                print(f"You need ${drink_cost:.2f} for a {customer_response} but you've paid only ${payment}")
            
        else:
            print(f"There isn't sufficient for a {customer_response}")
        
    elif customer_response == "off":
        coffee_machine_on = False