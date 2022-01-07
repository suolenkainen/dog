import unittest
import src.gene as gene
import src.player as player
import json


class gene_tests(unittest.TestCase):
    def setUp(self):        

        self.gene = gene.Gene()
        self.pool = gene.Pool()
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

    
    def test_newInnovation(self):

        innovation = gene.newInnovation()

        self.assertEqual(innovation, 5)

    
    def test_disjoint_identical(self):
        
        genes1 = []
        genes2 = []
        for n in range(3):
            local_gene = gene.Gene()
            local_gene.innovation = n
            genes1.append(local_gene)
            genes2.append(local_gene)

        result = gene.disjoint(genes1, genes2)
        self.assertEqual(result, 0)


    def test_disjoint_oneDiff(self):
        
        genes1 = []
        genes2 = []
    
        local_gene1 = gene.Gene()
        local_gene1.innovation = 5
        local_gene2 = gene.Gene()
        local_gene2.innovation = 6
        genes1.append(local_gene1)
        genes2.append(local_gene2)

        result = gene.disjoint(genes1, genes2)
        self.assertEqual(result, 2.0)

        
    def test_weight_identical(self):
        
        genes1 = []
        genes2 = []
    
        genes1 = []
        genes2 = []
        for n in range(1,4):
            local_gene = gene.Gene()
            local_gene.weight = round(1/n,3)
            local_gene.innovation = n
            genes1.append(local_gene)
            genes2.append(local_gene)

        result = gene.weights(genes1, genes2)
        self.assertEqual(result, 0)


    def test_weigh_oneInnovDiff(self):
        
        genes1 = []
        genes2 = []
    
        local_gene1 = gene.Gene()
        local_gene1.innovation = 5
        local_gene2 = gene.Gene()
        local_gene2.innovation = 6
        genes1.append(local_gene1)
        genes2.append(local_gene2)

        result = gene.weights(genes1, genes2)
        self.assertEqual(result, 1)


    def test_weigh_innovDiff(self):
        
        genes1 = []
        genes2 = []
    
        local_gene0 = gene.Gene()
        local_gene0.innovation = 5
        local_gene0.weight = round(1/2,3)
        local_gene1 = gene.Gene()
        local_gene1.innovation = 6
        local_gene1.weight = round(1/3,3)
        local_gene2 = gene.Gene()
        local_gene2.innovation = 6
        local_gene2.weight = round(2/3,3)

        genes1.append(local_gene0)
        genes1.append(local_gene1)
        genes2.append(local_gene2)

        result = gene.weights(genes1, genes2)
        self.assertEqual(result, 0.334)


    def test_sameSpecies(self):
        
        genes1 = []
        genes2 = []
    
        local_gene0 = gene.Gene()
        local_gene0.innovation = 5
        local_gene0.weight = round(1,3)
        local_gene1 = gene.Gene()
        local_gene1.innovation = 6
        local_gene1.weight = round(1/3,3)
        local_gene2 = gene.Gene()
        local_gene2.innovation = 6
        local_gene2.weight = round(2/3,3)

        genes1.append(local_gene0)
        genes1.append(local_gene1)
        genes2.append(local_gene2)

        player1 = player.Player()
        player2 = player.Player()

        player1.genes.append(local_gene0)
        player1.genes.append(local_gene1)
        player2.genes.append(local_gene2)

        result = self.pool.sameSpecies(player1, player2)
        self.assertEqual(result,  False)


if __name__ == '__main__':
    with open('C:\dog\dog\conf\global.json') as f:
        data = json.load(f)

    data["innovation"] = 4

    with open('C:\dog\dog\conf\global.json', 'w') as json_file:
        json.dump(data, json_file)

    unittest.main()