
# deal
def deal(player, deck):
    for _ in range(3):
        player.hand.append(deck.cards.pop(0))


def draw(player, deck):
    if len(player.hand) == 3 or len(player.hand) == 0:
        pass
    elif len(deck.cards) > 0:
        player.hand.append(deck.cards.pop(0))
    elif len(deck.cards) == 0 and deck.trump != ():
        player.stash.append(deck.trump)
        deck.trump = ()


def playCard(player, card, deck):
    if card == 3 and deck.cards != []:
        deck.table.append([deck.cards.pop(0), player.index])
    elif card != 3 and card <= len(player.hand):
        deck.table.append([player.hand.pop(card), player.index])
    else:
        while True:
            card -= 1
            if card == len(player.hand)-1:
                deck.table.append([player.hand.pop(card), player.index])
                break
            elif card == -1:
                break


def winTable(players, deck):
    
    largest_card = -1
    winning_index = -1
    for card in deck.table:
        [_,(number, _)], index = card
        if number > largest_card:
            largest_card = number
            winning_index = index
        elif number == largest_card:
            deck.tiebreaker = deck.table
            deck.table = []
    for tablecard, i in deck.table:
        players[winning_index].stash.append(tablecard)
        if players[winning_index].score == -10:
            players[winning_index].score = 0
        players[winning_index].score += tablecard[0]
    if winning_index != -1:
        players[winning_index].next = True
    else:
        players[winning_index].next = False

    deck.table = []
            
                



def tiebreakers(players, deck):
    deck.tiebreaker = []


def getInputs(players, deck):
    pass
