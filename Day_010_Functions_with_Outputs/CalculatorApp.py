#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multipy(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return round(n1 / n2)


operations = {
  "+": add,
  "-": subtract,
  "*": multipy,
  "/": divide
}

def calculator():
  print()
  n1 = float(input("Input first number: "))
  
  for operator in operations:
    print(operator)
  
  should_continue = True
  
  while should_continue:
    operator = input("Pick an operator from the options above: ") 
    n2 = float(input("Input second number: "))
    
    calc_function = operations[operator]
    answer1 = calc_function(n1, n2)

    print(f"{n1} {operator} {n2} = {answer1}")
    print()
  
    if input(f"Type 'y' to continue calculating with {answer1} or 'n' to restart the calculator: ") == "y":
      n1 = answer1
    else:
      should_continue = False
      calculator()

calculator()
