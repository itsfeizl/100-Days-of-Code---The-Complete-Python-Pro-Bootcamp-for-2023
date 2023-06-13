from prettytable import PrettyTable


class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def print_menu_ingredients(self):
        my_table = PrettyTable(["", "Water", "Milk", "Coffee"])
        my_table.align = "l"

        for item in self.menu:
            water = str(item.ingredients["water"])
            milk = str(item.ingredients["milk"])
            coffee = str(item.ingredients["coffee"])

            my_table.add_row([item.name.capitalize(), water, milk, coffee])

        print(my_table)

    def print_menu(self):
        menu_table = PrettyTable(["Beverage", "Price"])
        menu_table.title = "MENU"
        menu_table.align = "l"

        for product in self.menu:
            price = round(product.cost, 2)
            menu_table.add_row([product.name.capitalize(), price])

        print(menu_table)
        print()

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
