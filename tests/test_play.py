import unittest
import src.play as play
import src.player as plr
import src.deck as dck


### Tests for picture cards is missing

class Play(unittest.TestCase):
    def setUp(self):
        players = [plr.Player()]
        self.player = players[0]

        faces = [2,3,4]
        suits = ["hearts", "spades"]
        self.deck = dck.Deck(suits,faces)
        self.deck.shuffle()
        

    def test_deal(self):

        play.deal([self.player], self.deck)
        self.assertEqual(self.player.hand, [(4, 'hearts'), (3, 'hearts'), (2, 'hearts')])


    def test_draw_OK(self):

        self.player.hand = [(4, 'hearts'), (3, 'hearts'), (2, 'hearts')]
        self.deck.cards = [(4, 'spades'), (2, 'spades')]

        play.draw(self.player, self.deck)
        self.player.hand.pop(0)
        self.assertEqual(self.player.hand, [(3, 'hearts'), (2, 'hearts'), (4, 'spades')])


    def test_drawTrump(self):

        self.player.hand = [(4, 'hearts'), (3, 'hearts'), (2, 'hearts')]
        self.deck.cards = []
        self.deck.trump = (3, 'spades')

        play.draw(self.player, self.deck)
        self.assertEqual(self.player.hand, [(4, 'hearts'), (3, 'hearts'), (2, 'hearts')])
        self.assertEqual(self.player.stash, [(3, 'spades')])


    def test_draw_Empty(self):

        self.player.hand = [(4, 'hearts'), (3, 'hearts'), (2, 'hearts')]
        self.deck.cards = []
        self.deck.trump = ()
        
        play.draw(self.player, self.deck)
        self.player.hand.pop(0)
        self.assertEqual(self.player.hand, [(3, 'hearts'), (2, 'hearts')])
    

    def test_playCard(self):

        self.player.hand = [(4, 'hearts'), (3, 'hearts'), (2, 'hearts')]
        self.player.index = 0
        self.deck.table = []
        card = (4, 'hearts')

        play.playCard(self.player, card, self.deck)
        self.assertEqual(self.deck.table, [[(4, 'hearts'), 0]])
        self.assertEqual(self.player.hand, [(3, 'hearts'), (2, 'hearts')])


    def test_winTable_OK(self):
        players = []
        for i in range(3):
            player = plr.Player()
            player.index = i
            players.append(player)
        
        self.deck.table = [[(4, 'hearts'), 0], [(3, 'hearts'), 1], [(2, 'spades'), 2]]

        play.winTable(players, self.deck)
        self.assertEqual(self.deck.table, [])
        winning_player = players[0]
        self.assertEqual(winning_player.stash, [(4, 'hearts'),(3, 'hearts'),(2, 'spades')])


    def test_winTable_Tie(self):
        players = []
        for i in range(3):
            player = plr.Player()
            player.index = i
            players.append(player)
            player.hand = [(str(i+1), 'spades')]
        
        self.deck.table = [[(4, 'hearts'), 0], [(4, 'spades'), 1], [(3, 'spades'), 2]]

        play.winTable(players, self.deck)
        self.assertEqual(self.deck.table, [])
        self.assertEqual(self.deck.tiebreaker, [[(4, 'hearts'), 0], [(4, 'spades'), 1], [(3, 'spades'), 2]])
        winning_player = players[0]
        self.assertEqual(winning_player.stash, [])


    def test_score(self):
        players = []
        for i in range(2):
            player = plr.Player()
            player.index = i
            players.append(player)
            player.hand = [(str(i+1), 'spades')]
        
        self.deck.table = [[(4, 'hearts'), 0], [(3, 'spades'), 1]]

        play.winTable(players, self.deck)
        winning_player = players[0]
        self.assertEqual(winning_player.score, 7)


    def test_tiebreaker(self):
        pass

if __name__ == '__main__':
    unittest.main()