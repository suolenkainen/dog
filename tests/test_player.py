import unittest
import src.player as player


class Player(unittest.TestCase):
    def setUp(self):        

        self.player = player.Player()


    def test_createPlayer (self):
                
        # Test that player creation works as intended

        self.assertEqual(self.player.playernumber, 0)
        self.assertEqual(self.player.hand, [])
        self.assertEqual(self.player.stash, [])
        self.assertEqual(self.player.score, -10)
        self.assertEqual(self.player.neurons, {})
        self.assertEqual(self.player.connections, {})
    


if __name__ == '__main__':
    unittest.main()