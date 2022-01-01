"""This visualizes the card game in terminal and later to a text file"""

import random

# # variables
# faces = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]

# suits = ["hearts", "spades", "diamonds", "clubs"]
# suits_uni = ["\u2661", "\u2664", "\u2662", "\u2667"]

# variables
amount_of_players = 2
amount_of_card_in_hand = 3
faces = ["1","2","3","4","5"]

suits = ["hearts", "spades", "diamonds"]
suits_uni = ["\u2661", "\u2664", "\u2662"]

deck = []

for suit in suits_uni:
    for card in faces:
        print(suit, card)
        deck.append(suit + card)

print(deck)

# Shuffle the deck
random.shuffle(deck)
print(deck)

# Create hands for each player
players = []
for _ in range(amount_of_players):
    hand = []
    for _ in range(amount_of_card_in_hand):
        hand.append(deck.pop(0))
    players.append(hand)
    print(hand)
print(deck)
print(players)

