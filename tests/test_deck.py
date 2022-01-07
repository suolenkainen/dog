import unittest
import src.deck as deck


class Deck(unittest.TestCase):
    def setUp(self):        

        faces = [2,3]
        suits = ["hearts", "spades"]

        self.deck = deck.Deck(suits, faces)

    def test_createDeck (self):
                
        # Test that deck creation works as intended and returns a deck

        self.assertEqual(self.deck.cards, [[0, (2, 'hearts')], [1, (3, 'hearts')], [2, (2, 'spades')], [3, (3, 'spades')]])
        self.assertEqual(self.deck.faces, [2,3])
        self.assertEqual(self.deck.suits, ["hearts", "spades"])

    
    def test_shuffleDeck (self):

        # Test that shuffle works correctly

        self.deck.shuffle()

        self.assertEqual(self.deck.cards, [[0, (2, 'hearts')], [1, (3, 'hearts')], [3, (3, 'spades')]])
        self.assertEqual(self.deck.trump, [2, (2, 'spades')])
        self.assertEqual(self.deck.trumpsuit, "spades")
        

if __name__ == '__main__':
    unittest.main()