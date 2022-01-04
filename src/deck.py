import random

class Deck:
    def __init__(self, suits, faces):
        self.cards = []
        self.trump = ()
        self.table = []
        self.tiebreaker = []
        self.trumpsuit = ""
        self.scores = [-1, 0, -1]

        self.suits = suits
        self.faces = faces

        for suit in suits:
            for card in faces:
                self.cards.append((card, suit))
        
        self.score(faces)
    

    def shuffle(self, seed):
        random.seed(seed)
        random.shuffle(self.cards)
        self.trump = self.cards.pop(0)
        self.trumpsuit = self.trump[1]
    

    def score(self, faces):
        minimum = []
        medium = []
        maximum = []
        for _ in range(round(len(faces)/3)):
            minimum.append(faces.pop(0))
        for _ in range(round(len(faces)/3)):
            medium.append(faces.pop(0))
        maximum = faces
        self.scores = [minimum, medium, maximum]
        print([minimum, medium, maximum])
