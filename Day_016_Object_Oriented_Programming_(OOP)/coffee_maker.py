from prettytable import PrettyTable


class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report_table(self):
        report_table = PrettyTable(["Beverage", "Ingredients/Price"])
        report_table.title = "REPORT"
        report_table.align = "l"

        for item in self.resources:
            ing_level = str(self.resources[item]) + "ml"
            report_table.add_row([item, ing_level])

        print(report_table)

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if self.resources[item] == 0:
                print(f"Sorry, can't process your order because {item} container is empty.")
                print()
            elif drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, {item} level (at {self.resources[item]}ml) is insufficient for a {drink.name}")

                can_make = False
                
        return can_make


    def make_coffee(self, drink):
        """Deducts the required ingredients from the resources."""
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"And here is your {drink.name} ☕️.")
        print("Enjoy!")
        print()
