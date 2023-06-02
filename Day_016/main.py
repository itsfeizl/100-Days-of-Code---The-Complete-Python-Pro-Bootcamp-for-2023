from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()

money = 0
order_name = input("What would you like? (espresso/latte/cappuccino/):").lower()

if order_name == "report":
    coffee_maker.report()
    print(f"Money: ${money:.2f}")
    print()
