"""This visualizes the card game in terminal and later to a text file"""

import random
import deck as dck
import player as plr
import play
import src.pool as gn
import json
import network as nw

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

pool = gn.Pool()
for i in range(amount_of_players):
    local_player = plr.Player()
    local_player.index = i
    local_player.seed = i
    play.deal(local_player, deck_local)
    local_player.mutatePlayer()
    pool.addToSpecies(local_player)

play.deal(pool.opponent, deck_local)

players = []
for i in range(amount_of_players):
    local_player = plr.Player()
    local_player.index = i
    local_player.seed = i
    play.deal(local_player, deck_local)
    local_player.mutatePlayer()
    players.append(local_player)

# play.deal(players, deck_local)
# print(players)

# For loop where the game goes through
dropped_players = []
loop = True
while loop:
    break
    for player in players:
        if player.hand == []:
            continue
        # played_card = player.hand[0]
        play.playCard(player, 0, deck_local)
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
# for player in players:
#     print(player.__dict__)


# Run


while True:

    species = pool.species[pool.currentSpecies]
    player = species.players[pool.currentPlayer]
        
    played_card = nw.evaluateCurrent(pool, deck_local)
    opponent_card = nw.opponentCurrent(pool, deck_local)

    if player.next:
        play.playCard(player, played_card, deck_local)
        play.draw(player,deck_local)
        play.playCard(pool.opponent, opponent_card, deck_local)
        play.draw(pool.opponent, deck_local)
    else:
        play.playCard(pool.opponent, opponent_card, deck_local)
        play.draw(pool.opponent,deck_local)
        play.playCard(player, played_card, deck_local)
        play.draw(player,deck_local)

    play.winTable([player, pool.opponent], deck_local)

    if player.hand == []:
        
        if player.score > pool.maxFitness:
            pool.maxFitness = player.score
        
        print("Gen", pool.generation, ", species", pool.currentSpecies, ", player", pool.currentPlayer, ", fitness:", player.score)
        
        player.stash = []
        
        deck_local = []
        deck_local = dck.Deck(suits, faces)
        deck_local.shuffle()

        pool.currentSpecies = 1
        pool.currentPlayer = 1
        # while fitnessAlreadyMeasured():
        # 	nextplayer()
        # initializeRun()
        break


    




# Kun on p????tetty, kuka on paras, se otetaan kaikille vastustajaksi. 
# K??yt??nn??ss?? siis yks niist?? pelaa kerran itse????n vastaan
# Jos kortti on k??dess??, siit?? tulee positiivinen signaali, jos p??yd??ss??, negatiivinen


with open('C:\dog\dog\conf\global.json') as f:
    data = json.load(f)

data["innovation"] = 4

with open('C:\dog\dog\conf\global.json', 'w') as json_file:
    json.dump(data, json_file)
    