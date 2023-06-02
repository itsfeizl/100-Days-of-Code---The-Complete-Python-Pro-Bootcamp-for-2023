import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has Blackjack. Sorry, you lose!"
    elif player_score == 0:
        return "You with with a Blackjack!"
    elif player_score > 21:
        return "Your tally is over 21. You lose!"
    elif computer_score > 21:
        return "Computer tally is over 21. You win!"
    elif player_score > computer_score:
        return "Your tally is greater than computer's tally. You win!"
    else:
        return "Your tally is less that computer's tally. You lose!"


def play_game():
    player_cards = []
    computer_cards = []
    game_over = False


    for _ in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not game_over:

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"  Your cards: {player_cards}, current score: {player_score}")
        print(f"  Computer's first card {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            draw_card = input("Do you want to draw another card? Type 'Y' or 'N': " ).lower()
            if draw_card == "y":
                player_cards.append(deal_cards())
            else:
                game_over = True
            

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)


    print(f"Your final cards: {player_cards}; Your final score: {player_score}")
    print(f"Computer final cards: {computer_cards}, computer final score: {computer_score}")
    print(compare(player_score, computer_score))

play = input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").lower()
while play == "y":
    play_game()