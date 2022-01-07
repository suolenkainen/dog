import unittest
import src.pool as pool
import src.player as player
import json


class gene_tests(unittest.TestCase):
    def setUp(self):        

        self.gene = player.Gene()
        self.pool = pool.Pool()
        self.player = player.Player()


    def test_createGene (self):
                
        self.assertEqual(self.gene.sink, 0)
        self.assertEqual(self.gene.source, 0)
        self.assertEqual(self.gene.weight, 0.0)
        self.assertEqual(self.gene.enabled, True)
        self.assertEqual(self.gene.innovation, 0)
   

    def test_createPool(self):
        
        self.assertEqual(self.pool.species, [])
        self.assertEqual(self.pool.generation, 0)
        self.assertEqual(self.pool.innovation, 4)
        self.assertEqual(self.pool.currentSpecies, 1)
        self.assertEqual(self.pool.currentPlayer, 1)
        self.assertEqual(self.pool.currentFrame, 0)
        self.assertEqual(self.pool.maxFitness, 0)


    
if __name__ == '__main__':
    with open('C:\dog\dog\conf\global.json') as f:
        data = json.load(f)

    data["innovation"] = 4

    with open('C:\dog\dog\conf\global.json', 'w') as json_file:
        json.dump(data, json_file)

    unittest.main()