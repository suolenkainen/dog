"""This visualizes the card game in terminal and later to a text file"""

import deck as dck
import player as plr
import play
import gene as gn

# # variables
# faces = ["2","3","4","5","6","7","8","9","10","J","Q","K"]

# suits = ["hearts", "spades", "diamonds", "clubs"]
# suits_uni = ["\u2661", "\u2664", "\u2662", "\u2667"]

# variables
amount_of_players = 2
amount_of_card_in_hand = 3
faces = [2,3,4,5,6,7,8,9,10,11,12,13,14]

suits = ["hearts", "spades", "diamonds", "clubs"]
suits_uni = ["\u2661", "\u2664", "\u2662"]

deck_local = []
deck_local = dck.Deck(suits, faces)
deck_local.shuffle()
print(deck_local.trump)

players = []
for i in range(amount_of_players):
    local_player = plr.Player()
    local_player.index = i
    local_player.mutatePlayer()
    players.append(local_player)

play.deal(players, deck_local)
print(players)

# For loop where the game goes through
dropped_players = []
loop = True
while loop:
    for player in players:
        if player.hand == []:
            continue
        played_card = player.hand[0]
        play.playCard(player, played_card, deck_local)
        play.draw(player,deck_local)
        # print(player.__dict__)
    play.winTable(players, deck_local)
    # while True:
    #     if deck_local.tiebreaker is not []:
    #         for player in players:
    #             if player.hand == []:
    #                 continue
    #             played_card = player.hand[0]
    #             play.playCard(player, played_card, deck_local)
    #             play.draw(player,deck_local)
    #         play.tiebreakers(players, deck_local)
        # else:
        #     break
    for player in players:
        if len(dropped_players) == len(players):
            loop = False
        if player.hand == []:
            dropped_players.append(player.index)
for player in players:
    print(player.__dict__)
    
    