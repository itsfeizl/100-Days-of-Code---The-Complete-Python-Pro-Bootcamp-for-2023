
machine_started = True

while machine_started:

    print("Coffee machine off.")
    start_machine = input("Enter 'ON' to turn on: ").lower()
    print()

    if start_machine == "on":

        machine_on = True
        while machine_on == True:

            print("Coffee machine started.")
            options = input("To check menu, enter 'MENU'; to place an order, enter 'ORDER';\nOr enter 'OFF' to turn machine off: ").lower()

            if options == "off":
                machine_on = False
