import unittest
import src.pool as pool
import src.player as plr
import src.utils as utils
import json


class Utils(unittest.TestCase):
    def setUp(self):        

        self.gene = plr.Gene()
        self.pool = pool.Pool()
        self.player = plr.Player()

    
    def test_disjoint_identical(self):
        
        genes1 = []
        genes2 = []
        for n in range(3):
            local_gene = plr.Gene()
            local_gene.innovation = n
            genes1.append(local_gene)
            genes2.append(local_gene)

        result = utils.disjoint(genes1, genes2)
        self.assertEqual(result, 0)


    def test_disjoint_oneDiff(self):
        
        genes1 = []
        genes2 = []
    
        local_gene1 = plr.Gene()
        local_gene1.innovation = 5
        local_gene2 = plr.Gene()
        local_gene2.innovation = 6
        genes1.append(local_gene1)
        genes2.append(local_gene2)

        result = utils.disjoint(genes1, genes2)
        self.assertEqual(result, 2.0)

        
    def test_weight_identical(self):
        
        genes1 = []
        genes2 = []
    
        genes1 = []
        genes2 = []
        for n in range(1,4):
            local_gene = plr.Gene()
            local_gene.weight = round(1/n,3)
            local_gene.innovation = n
            genes1.append(local_gene)
            genes2.append(local_gene)

        result = utils.weights(genes1, genes2)
        self.assertEqual(result, 0)


    def test_weigh_oneInnovDiff(self):
        
        genes1 = []
        genes2 = []
    
        local_gene1 = plr.Gene()
        local_gene1.innovation = 5
        local_gene2 = plr.Gene()
        local_gene2.innovation = 6
        genes1.append(local_gene1)
        genes2.append(local_gene2)

        result = utils.weights(genes1, genes2)
        self.assertEqual(result, 1)


    def test_weigh_innovDiff(self):
        
        genes1 = []
        genes2 = []
    
        local_gene0 = plr.Gene()
        local_gene0.innovation = 5
        local_gene0.weight = round(1/2,3)
        local_gene1 = plr.Gene()
        local_gene1.innovation = 6
        local_gene1.weight = round(1/3,3)
        local_gene2 = plr.Gene()
        local_gene2.innovation = 6
        local_gene2.weight = round(2/3,3)

        genes1.append(local_gene0)
        genes1.append(local_gene1)
        genes2.append(local_gene2)

        result = utils.weights(genes1, genes2)
        self.assertEqual(result, 0.334)


    def test_sameSpecies(self):

        confs = {}
        confs["DeltaDisjoint"] = self.pool.DeltaDisjoint
        confs["DeltaWeights"] = self.pool.DeltaWeights
        confs["DeltaThreshold"] = self.pool.DeltaThreshold
        
        genes1 = []
        genes2 = []
    
        local_gene0 = plr.Gene()
        local_gene0.innovation = 5
        local_gene0.weight = round(1,3)
        local_gene1 = plr.Gene()
        local_gene1.innovation = 6
        local_gene1.weight = round(1/3,3)
        local_gene2 = plr.Gene()
        local_gene2.innovation = 6
        local_gene2.weight = round(2/3,3)

        genes1.append(local_gene0)
        genes1.append(local_gene1)
        genes2.append(local_gene2)

        player1 = plr.Player()
        player2 = plr.Player()

        player1.genes.append(local_gene0)
        player1.genes.append(local_gene1)
        player2.genes.append(local_gene2)

        result = utils.sameSpecies(confs, player1, player2)
        self.assertEqual(result,  False)


    def test_newInnovation(self):

        innovation = utils.newInnovation()

        self.assertEqual(innovation, 8)


    def test_sigmoid(self):

        print(utils.sigmoid(0.1))
        print(utils.sigmoid(1.0))


if __name__ == '__main__':
    with open('C:\dog\dog\conf\global.json') as f:
        data = json.load(f)

    data["innovation"] = 4

    with open('C:\dog\dog\conf\global.json', 'w') as json_file:
        json.dump(data, json_file)

    unittest.main()