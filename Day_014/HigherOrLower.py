from art import logo, vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')


score = 0

def generate_random_num():
  return random.randint(0, (len(data) - 1))

def generate_option():
    celebrity = data[generate_random_num()]
    return celebrity

option_a = generate_option()
option_b = generate_option()

if option_b == option_a:
    option_b = generate_option()

print(logo)

#Comparing options A and B

def compare(option_a, option_b):
    
    print("Compare A: " + option_a["name"] + ", a " + option_a["description"] + " from " + option_a["country"] + ".")
    
    print(vs)

    print("Compare B: " + option_b["name"] + ", a " + option_b["description"] + " from " + option_b["country"] + ".")




#Creating a loop
continue_playing = True



while continue_playing == True:
    
    compare(option_a, option_b)

    #Asking for player response
    player_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    clear()
    print(logo)
    #Checking player input
    if player_input == "A":
        
        if option_a["follower_count"] > option_b["follower_count"]:
            score += 1
            
            print(f"You're right! Current score: {score}")
            option_a = option_b
            option_b = generate_option()
            if option_b == option_a:
                option_b = generate_option()
        else:
            continue_playing = False
            print(f"Sorry, that's wrong. Final score: {score}")
    elif player_input == "B":
        if option_b["follower_count"] > option_a["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}.")
            option_a = option_b
            option_b = generate_option()
            if option_b == option_a:
                option_b = generate_option()
        else:
            continue_playing = False
            print(f"Sorry, that's wrong. Final score: {score}.")


