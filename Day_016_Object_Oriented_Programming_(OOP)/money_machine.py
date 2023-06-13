from prettytable import PrettyTable
import os
clear = lambda: os.system('cls')

class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"| Money    | {self.CURRENCY}{self.profit}                |")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        print()
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        print()
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        add_more_coins = True
        while add_more_coins:
            self.process_coins()
            if self.money_received == cost:
                clear()
                print("Payment received.")
                return True
            elif self.money_received >= cost:
                clear()
                print("Payment received.")
                change = round(self.money_received - cost, 2)
                print(f"Here is {self.CURRENCY}{change} in change.")
                self.profit += cost
                self.money_received = 0
                return True
            else:
                print("Sorry that's not enough money.")
                more_coins = input("Would you like to add more coins? Enter 'YES' or 'NO': ").lower()
                print()
                if more_coins == "yes":
                    add_more_coins = True
                else:
                    add_more_coins = False
                    print(f"Sorry, money paid (${self.money_received}) is not enough to process your order.")
                    print("Money refunded.")
                    print()
                    self.money_received = 0
                    return False
