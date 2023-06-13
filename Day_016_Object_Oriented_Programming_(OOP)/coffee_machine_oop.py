from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

import os

clear = lambda: os.system('cls')

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
menu_item = MenuItem("name", "water", "milk", "coffee", "cost")

money = 0

machine_started = True

while machine_started:

    print("Coffee machine off.")
    start_machine = input("Enter 'ON' to turn on: ").lower()
    print()

    if start_machine == "on":

        machine_on = True

        while machine_on:

            options = ""

            print("Coffee machine on.")
            prompt = input("To check menu, enter 'MENU'; to place an order, enter 'ORDER';\n"
                           "Or enter 'OFF' to turn machine off: ").lower()
            print()

            if prompt == "off":
                print("Turning coffee machine off...")
                print()
                machine_on = False

            elif prompt == "report":
                coffee_maker.report_table()
                money_machine.report()
                print("+----------+-------------------+")
                print()

            elif prompt == "menu":

                menu.print_menu()
                order_now = input("Would you like to place an order? Enter 'YES' or 'NO': ").lower()
                print()

                if order_now == "yes":
                    options = "order"

            if prompt == "order" or options == "order":

                place_order = True

                while place_order:
                    order_name = input("What would you like? (" + menu.get_items() + "): ").lower()
                    print()

                    if order_name == "espresso" or order_name == "latte" or order_name == "cappuccino":

                        drink = menu.find_drink(order_name)

                        if coffee_maker.is_resource_sufficient(drink):

                            order_price = menu.find_drink(order_name).cost

                            print(f"Your order: {order_name.capitalize()}.")
                            print(f"Price: ${order_price:.2f}.")
                            print()

                            if money_machine.make_payment(order_price):
                                coffee_maker.make_coffee(drink)

                                place_another_order = input("Would you like to place another order? Enter 'YES' or "
                                                            "'No: ").lower()

                                if place_another_order == "yes":
                                    print()
                                    continue
                                elif place_another_order == "no":
                                    print()
                                    place_order = False

                        else:
                            print()
                            print("You can still try some of our other refreshing beverages.")
                            print("Here's a table of our menu showing the ingredient requirement to help you decide.")
                            menu.print_menu_ingredients()
                            print()

                    elif order_name == "off":
                        clear()
                        place_order = False
            elif options == "off":
                machine_on = False
