import unittest
import src.player as player
import src.pool as pool
import json


class Player(unittest.TestCase):
    def setUp(self):        

        self.player = player.Player()


    def test_createPlayer (self):
                
        # Test that player creation works as intended

        self.assertEqual(self.player.index, -1)
        self.assertEqual(self.player.hand, [])
        self.assertEqual(self.player.stash, [])
        self.assertEqual(self.player.score, -10)
        self.assertEqual(self.player.seed, 0)
        
        MutateConnectionsChance = 0.25
        LinkMutationChance = 2.0
        NodeMutationChance = 0.50
        BiasMutationChance = 0.40
        StepSize = 0.1
        DisableMutationChance = 0.4
        EnableMutationChance = 0.2

        self.assertEqual(self.player.genes, [])
        self.assertEqual(self.player.fitness, 0)
        self.assertEqual(self.player.adjustedFitness, 0)
        self.assertEqual(self.player.network, {})
        self.assertEqual(self.player.maxneuron, 209)
        self.assertEqual(self.player.globalRank, 0)
        self.assertEqual(self.player.mutationRates["connections"], MutateConnectionsChance)
        self.assertEqual(self.player.mutationRates["link"], LinkMutationChance)
        self.assertEqual(self.player.mutationRates["bias"], BiasMutationChance)
        self.assertEqual(self.player.mutationRates["node"], NodeMutationChance)
        self.assertEqual(self.player.mutationRates["enable"], EnableMutationChance)
        self.assertEqual(self.player.mutationRates["disable"], DisableMutationChance)
        self.assertEqual(self.player.mutationRates["step"], StepSize)

    
    def test_mutatePlayerRates(self):

        self.player.mutationRates["connections"] = 2.0
        self.player.mutationRates["link"] = 2.0
        self.player.mutationRates["bias"] = 2.0
        self.player.mutationRates["node"] = 2.0
        self.player.mutationRates["enable"] = 2.0
        self.player.mutationRates["disable"] = 2.0
        self.player.mutationRates["step"] = 2.0
        
        self.player.mutatePlayer()
        self.assertEqual(self.player.mutationRates["connections"], 2.10526)
        self.assertEqual(self.player.mutationRates["link"], 2.10526)
        self.assertEqual(self.player.mutationRates["bias"], 1.9)
        self.assertEqual(self.player.mutationRates["node"], 2.10526)
        self.assertEqual(self.player.mutationRates["enable"], 2.10526)
        self.assertEqual(self.player.mutationRates["disable"], 2.10526)
        self.assertEqual(self.player.mutationRates["step"], 2.10526)
    

    def test_pointMutate(self):
        
        self.player.mutationRates["step"] = 0.1

        local_gene = player.Gene()
        local_gene.sink = 0
        local_gene.source = 0
        local_gene.weight = 0.0
        local_gene.enabled = True
        local_gene.innovation = 0

        self.player.genes.append(local_gene)
        
        self.player.pointMutate()
        self.assertEqual(self.player.genes[0].weight, 0.05159)
    

    def test_linkMutate_Bias(self):

        self.player.linkMutate(True)

        self.assertEqual(self.player.genes[0].enabled, True)
        self.assertEqual(self.player.genes[0].innovation, 5)
        self.assertEqual(self.player.genes[0].sink, 209)
        self.assertEqual(self.player.genes[0].source, 1000004)
        self.assertEqual(self.player.genes[0].weight, 1.03182)


    def test_linkMutate_noBias(self):

        self.player.linkMutate(False)

        self.assertEqual(self.player.genes[0].enabled, True)
        self.assertEqual(self.player.genes[0].innovation, 6)
        self.assertEqual(self.player.genes[0].sink, 95)
        self.assertEqual(self.player.genes[0].source, 1000004)
        self.assertEqual(self.player.genes[0].weight, 1.03182)

    
    def test_randomNeuron_true(self):

        result = self.player.randomNeuron(True)
        self.assertEqual(result, 1000004)


    def test_randomNeuron_false(self):

        result = self.player.randomNeuron(False)        
        self.assertEqual(result, 95)


    def test_randomNeuron_True_genes(self):

        local_gene = player.Gene()
        local_gene.sink = 4
        local_gene.source = 57
        local_gene.weight = 0.0
        local_gene.enabled = True
        local_gene.innovation = 0
        self.player.genes.append(local_gene)

        result = self.player.randomNeuron(False)        
        self.assertEqual(result, 95)


    def test_containsLink_True(self):

        local_gene = player.Gene()
        local_gene.sink = 4
        local_gene.source = 57
        local_gene.weight = 0.0
        local_gene.enabled = True
        local_gene.innovation = 0
        self.player.genes.append(local_gene)

        result = self.player.containsLink(local_gene)
        self.assertEqual(result, True)


    def test_containsLink_False(self):

        local_gene = player.Gene()
        local_gene.sink = 4
        local_gene.source = 57
        local_gene.weight = 0.0
        local_gene.enabled = True
        local_gene.innovation = 0

        result = self.player.containsLink(local_gene)
        self.assertEqual(result, None)


    def test_copygene(self):

        local_gene = player.Gene()
        local_gene.sink = 4
        local_gene.source = 57
        local_gene.weight = 0.0
        local_gene.enabled = True
        local_gene.innovation = 0

        result = self.player.copyGene(local_gene)
        self.assertEqual(local_gene.sink, result.sink)
        self.assertEqual(local_gene.source, result.source)
        self.assertEqual(local_gene.weight, result.weight)
        self.assertEqual(local_gene.enabled, result.enabled)
        self.assertEqual(local_gene.innovation, result.innovation)

    
    def test_nodeMutate_noGenes(self):
        
        results = self.player.nodeMutate()

        self.assertEqual(results, None)


    def test_nodeMutate(self):
        
        local_gene = player.Gene()
        local_gene.sink = 1000004
        local_gene.source = 2
        local_gene.weight = 0.0
        local_gene.enabled = True
        local_gene.innovation = 0
        self.player.genes.append(local_gene)

        self.player.nodeMutate()

        self.assertEqual(self.player.maxneuron, 210)
        self.assertEqual(self.player.genes[0].enabled, False)

        self.assertEqual(self.player.genes[1].enabled, True)
        self.assertEqual(self.player.genes[1].innovation, 13)
        self.assertEqual(self.player.genes[1].sink, 1000004)
        self.assertEqual(self.player.genes[1].source, 210)
        self.assertEqual(self.player.genes[1].weight, 1.0)
        
        self.assertEqual(self.player.genes[2].enabled, True)
        self.assertEqual(self.player.genes[2].innovation, 14)
        self.assertEqual(self.player.genes[2].sink, 210)
        self.assertEqual(self.player.genes[2].source, 2)
        self.assertEqual(self.player.genes[2].weight, 0.0)


    def test_enabledDisableMutate_empty(self):

        result = self.player.enableDisableMutate(True)

        self.assertEqual(result, None)


    def test_enabledDisableMutate_1False(self):

        local_gene = player.Gene()
        local_gene.enabled = False
        self.player.genes.append(local_gene)
        self.player.enableDisableMutate(True)

        self.assertEqual(self.player.genes[0].enabled, True)


    def test_enabledDisableMutate_TrueFalse(self):

        local_gene1 = player.Gene()
        local_gene1.enabled = False
        self.player.genes.append(local_gene1)
        
        local_gene2 = player.Gene()
        local_gene2.enabled = True
        self.player.genes.append(local_gene2)

        self.player.enableDisableMutate(True)

        self.assertEqual(self.player.genes[0].enabled, True)
        self.assertEqual(self.player.genes[1].enabled, True)
        

if __name__ == '__main__':
    with open('C:\dog\dog\conf\global.json') as f:
        data = json.load(f)

    data["innovation"] = 4

    with open('C:\dog\dog\conf\global.json', 'w') as json_file:
        json.dump(data, json_file)

    unittest.main()