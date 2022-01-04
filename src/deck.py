import random

class Deck:
    def __init__(self, suits, faces):
        self.cards = []
        self.trump = ()
        self.table = []
        self.tiebreaker = []
        self.trumpsuit = ""

        self.suits = suits
        self.faces = faces

        for suit in suits:
            for card in faces:
                self.cards.append((card, suit))
    

    def shuffle(self, seed):
        random.seed(seed)
        random.shuffle(self.cards)
        self.trump = self.cards.pop(0)
        self.trumpsuit = self.trump[1]
