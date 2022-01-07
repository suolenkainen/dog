import unittest
import src.species as spc


class Species(unittest.TestCase):
    def setUp(self):

        self.species = spc.Species()
    
    def test_newSpecies(self):

        self.assertEqual(self.species.topFitness, 0)
        self.assertEqual(self.species.staleness, 0)
        self.assertEqual(self.species.players, [])
        self.assertEqual(self.species.averageFitness, 0)


if __name__ == '__main__':
    unittest.main()