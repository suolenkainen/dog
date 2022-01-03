"""This visualizes the card game in terminal and later to a text file"""

import deck
import player
import play

# # variables
# faces = ["2","3","4","5","6","7","8","9","10","J","Q","K"]

# suits = ["hearts", "spades", "diamonds", "clubs"]
# suits_uni = ["\u2661", "\u2664", "\u2662", "\u2667"]

# variables
amount_of_players = 2
amount_of_card_in_hand = 3
faces = ["2","3","4","5"]

suits = ["hearts", "spades", "diamonds"]
suits_uni = ["\u2661", "\u2664", "\u2662"]

deck_local = []
deck_local = deck.Deck(suits, faces)
deck_local.cards.shuffle(0)
print(deck_local.trump)

players = []
for i in range(amount_of_players):
    local_player = player.Player()
    local_player.index = i
    players.append(local_player)

play.deal(players, deck_local.cards)
print(players)

# For loop where the game goes through