# Initialize the VEX EXP Brain
brain = Brain()

def create_uno_deck():
    colors = ['Red', 'Yellow', 'Green', 'Blue']
    values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', '+2']
    deck = []

    # Add colored cards
    for color in colors:
        # One '0' card per color
        deck.append(color + " 0")
       
        # Two of each 1-9, Skip, Reverse, and +2 per color
        for val in values:
            deck.append(color + " " + val)
            deck.append(color + " " + val)

    # Add 4 Wild and 4 Wild +4 cards
    for i in range(4):
        deck.append("Wild")
        deck.append("Wild +4")

    return deck

def shuffle_deck(deck):
    # Fisher-Yates shuffle implemented for VEX MicroPython
    deck_length = len(deck)
    for i in range(deck_length - 1, 0, -1):
        j = random.randint(0, i)
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp

def setup_game():
    # 1. Create deck
    deck = create_uno_deck()
   
    # 2. Shuffle cards safely
    shuffle_deck(deck)

    # 3. Define players
    players = ["VEX Robot", "Player 1", "Player 2"]
    hands = {}
    for player in players:
        hands[player] = []

    # 4. Deal 7 cards to everyone playing
    cards_per_player = 7
    for i in range(cards_per_player):
        for player in players:
            if len(deck) > 0:
                card = deck.pop()
                hands[player].append(card)

    # 5. Display status on VEX EXP Brain Screen
    draw_count = len(deck)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("UNO Setup Complete!")
    brain.screen.set_cursor(2, 1)
    brain.screen.print("Draw Pile: " + str(draw_count) + " cards")

    # 6. Output detailed hands to Terminal
    print("=== UNO GAME INITIALIZED ===")
   
    total_dealt = 0
    for player in players:
        total_dealt = total_dealt + len(hands[player])

    total_cards = draw_count + total_dealt
   
    print("Total cards in deck: " + str(total_cards))
    print("Remaining in Draw Pile: " + str(draw_count))
    print("")

    for player in players:
        print("--- " + str(player) + "'s Hand ---")
        player_hand = hands[player]
        for card in player_hand:
            print("  - " + str(card))
        print("")

    print("Dealing complete. Robot stopped.")

# Run the setup function
setup_game()
