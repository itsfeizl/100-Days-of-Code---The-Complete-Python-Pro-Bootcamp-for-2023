# Code for Reeboks Hurdle 1 Challenge at: https://reeborg.ca/index_en.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for hurdles in range (0, 6):
    jump()