import unittest
import src.network as nw
import src.player as plr
import src.deck as dck
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
        self.assertEqual(len(self.player.network.neurons), 213)
        self.assertNotEqual(self.player.network.neurons[56].incoming, [])
        self.assertNotEqual(self.player.network.neurons[57].incoming, [])
        self.assertNotEqual(self.player.network.neurons[54].incoming, [])
        self.assertNotEqual(self.player.network.neurons[55].incoming, [])


    def test_getinputs(self):

        player = plr.Player()
        player.hand = [[12, (14, 'hearts')], [45, (8, 'clubs')],[41, (4, 'clubs')]]

        deck = dck.Deck([],[])
        deck.table = [[[38, (12, 'diamonds')],1]]

        result = nw.getInputs(player, deck)
        self.assertEqual(result[12], 1)
        self.assertEqual(result[97], 1)
        self.assertEqual(result[145], 1)
        self.assertEqual(result[194], 1)


    def test_evaluateNetwork(self):

        
        random.seed(0)
        for x in range(4):
            local_gene = plr.Gene()
            local_gene.sink = 10+x
            local_gene.source = 1000001 + x
            local_gene.weight = 0.5
            local_gene.enabled = True
            local_gene.innovation = 0
            self.player.genes.append(local_gene)

        for x in range(5,10):
            local_gene = plr.Gene()
            local_gene.sink = 8+x
            local_gene.source = 1000000 + x
            local_gene.weight = 0.1 * x
            local_gene.enabled = True
            local_gene.innovation = 0
            self.player.genes.append(local_gene)

        random.shuffle(self.player.genes)

        nw.generateNetwork(self.player)
        self.player.hand = [[12, (14, 'hearts')], [45, (8, 'clubs')],[41, (4, 'clubs')]]

        deck = dck.Deck([],[])
        deck.table = [[[38, (12, 'diamonds')],1]]

        inputs = nw.getInputs(self.player, deck)

        output = nw.evaluateNetwork(self.player.network, inputs)

        self.assertEqual(output, 3)


        ### TODO: Lots of tests
    
if __name__ == '__main__':
    unittest.main()