# In Python, variables can be declared without being assigned values so long as their data types
# have been indicated

age: int
name: str
employed: bool

# In the above, the variables have been declared without being assigned values.
# Only their types have been indicated


def check(age: int):
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(check(18))
