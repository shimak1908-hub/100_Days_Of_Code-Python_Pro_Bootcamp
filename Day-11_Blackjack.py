import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/      
"""

cards = [11 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

# Main game loop
play_game = True

while play_game:
    print(logo)

    # Deal cards
    player_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards), random.choice(cards)]

    game_over = False

    # Player turn
    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"\nYour cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 21:
            print("Blackjack! You have 21!")
            break
        elif player_score > 21:
            print("You went over 21. You lose ❌")
            game_over = True
            break

        another_card = input("Type 'y' to get another card, Type 'n' to pass: ").lower()
        if another_card == 'y':
            player_cards.append(random.choice(cards))
        else:
            game_over = True

    # Dealer turn
    while calculate_score(dealer_cards) < 17 and player_score <= 21:
        dealer_cards.append(random.choice(cards))

    # Final scores
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    # Determine winner
    if player_score > 21:
        print("You went over 21. Dealer wins ❌")
    elif dealer_score > 21:
        print("Dealer went over 21. You win ✅")
    elif player_score > dealer_score:
        print("You win! 🎉")
    elif dealer_score > player_score:
        print("Dealer wins ❌")
    else:
        print("It's a draw! 🤝")

    # Ask to play again
    replay = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if replay != 'y':
        play_game = False
        print("Thanks for playing! 👋")


# Player's turn
game_over = False

while not game_over:
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"\nYour cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    if player_score == 21:
        print("Blackjack! You have 21!")
        break
    elif player_score > 21:
        print("You went over 21. You lose ❌")
        game_over = True
        break

    another_card = input("Type 'y' to get another card, Type 'n' to pass: ").lower()
    if another_card == 'y':
        player_cards.append(random.choice(cards))
    else:
        game_over = True

# Dealer's turn
while calculate_score(dealer_cards) < 17 and player_score <= 21:
    dealer_cards.append(random.choice(cards))

# Final scores
player_score = calculate_score(player_cards)
dealer_score = calculate_score(dealer_cards)
print(f"\nYour final hand: {player_cards}, final score: {player_score}")
print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

# Determine winner
if player_score > 21:
    print("You went over 21. Dealer wins ❌")
elif dealer_score > 21:
    print("Dealer went over 21. You win ✅")
elif player_score > dealer_score:
    print("You win! 🎉")
elif dealer_score > player_score:
    print("Dealer wins ❌")
else:
    print("It's a draw! 🤝")

