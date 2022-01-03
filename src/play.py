

# deal
def deal(players, deck):
    for player in players:
        for _ in range(3):
            player.hand.append(deck.cards.pop(0))


def draw(player, deck):
    if len(deck.cards) > 0:
        player.hand.append(deck.cards.pop(0))
    elif deck.trump != ():
        player.hand.append(deck.trump)
        deck.trump = ()


def playCard(player, card, deck):
    player.hand.remove(card)
    deck.table.append([card, player.index])


def winTable(players, deck):
    if len(deck.table) < len(players):
        pass
    else:
        largest_card = -1
        winning_index = -1
        sorted(deck.table, key=lambda x: x[0])
        for card in deck.table:
            (number, _), index = card
            if int(number) > largest_card:
                largest_card = int(number)
                winning_index = index
            elif int(number) == largest_card:
                return False
        for tablecard, i in deck.table:
            players[winning_index].stash.append(tablecard)
        deck.table = []
            
                



def tiebreakers(players, deck):
    pass

    


#