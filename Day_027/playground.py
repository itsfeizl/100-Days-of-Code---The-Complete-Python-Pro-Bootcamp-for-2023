# Set unlimited number of arguments with *args
def add(*args):
    print(type(args))
    total = 0
    for n in args:
        total += n
    return total


print(add(2, 3, 4, 5, 6))
print(add(7, 8, 9, 10, 11, 12))


# Set unlimited number of key word arguments with **kwargs
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(7, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")  # or you can use kwargs["make"]
        self.model = kwargs.get("model")
        # The advantage of using the .get method is if nothing is specified for when initializing the class,
        # the code won't throw an error. It'll instead return none


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)