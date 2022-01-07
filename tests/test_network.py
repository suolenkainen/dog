import unittest
import src.network as nw
import src.player as plr
import random

class gene_tests(unittest.TestCase):
    def setUp(self):        
        
        self.player = plr.Player()

    def test_generateNetwork(self):

        random.seed(0)
        for x in range(4):
            local_gene = plr.Gene()
            local_gene.sink = 4+x
            local_gene.source = 57-x
            local_gene.weight = 0.0
            local_gene.enabled = True
            local_gene.innovation = 0
            self.player.genes.append(local_gene)

        random.shuffle(self.player.genes)

        nw.generateNetwork(self.player)

        print(self.player)
        self.assertEqual(len(self.player.network.neurons), 61)
        self.assertNotEqual(self.player.network.neurons[56].incoming, [])
        self.assertNotEqual(self.player.network.neurons[57].incoming, [])
        self.assertNotEqual(self.player.network.neurons[54].incoming, [])
        self.assertNotEqual(self.player.network.neurons[55].incoming, [])

    
if __name__ == '__main__':
    unittest.main()