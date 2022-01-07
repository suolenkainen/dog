# write neurons and connections
import json
import src.species as spc

class Pool:
    def __init__(self):
        self.species = []
        self.opponent = []
        self.generation = 0
        self.innovation = 4
        self.currentSpecies = 1
        self.currentPlayer = 1
        self.currentOpponent = 1
        self.currentFrame = 0
        self.maxFitness = 0
        
        self.DeltaDisjoint = 2.0
        self.DeltaWeights = 0.4
        self.DeltaThreshold = 1.0
    

    def addToSpecies(self, child):
        
        foundSpecies = False
        for species in self.species:
            if self.sameSpecies(child, species.players[0]):
                species.players.append(child)
                foundSpecies = True
                break
        
        if not foundSpecies:
            childSpecies = spc.Species()
            childSpecies.players.append(child)
            self.species.append(childSpecies)


    def sameSpecies(self, player1, player2):
        dd = self.DeltaDisjoint*disjoint(player1.genes, player2.genes)
        dw = self.DeltaWeights*weights(player1.genes, player2.genes) 
        return dd + dw < self.DeltaThreshold


def disjoint(genes1, genes2):
    i1 = []
    for temp_gene in genes1:
        i1.append(temp_gene.innovation)

    i2 = []
    for temp_gene in genes2:
        i2.append(temp_gene.innovation)
    
    disjointGenes = 0
    for temp_gene in genes1:
        if temp_gene.innovation not in i2:
            disjointGenes = disjointGenes + 1
    
    for temp_ in genes2:
        if temp_.innovation not in i1:
            disjointGenes = disjointGenes + 1
    
    n = max(len(genes1), len(genes2))
    if n == 0:
        return 1
    disj = round(disjointGenes / n, 5)

    return disj

def weights(genes1, genes2):
    i2 = {}
    for temp_gene2 in genes2:
        i2[temp_gene2.innovation] = temp_gene2

    sum = 0
    coincident = 0
    for temp_gene1 in genes1:
        if temp_gene1.innovation in i2.keys():
            temp_gene2 = i2[temp_gene1.innovation]
            sum = sum + abs(temp_gene1.weight - temp_gene2.weight)
            coincident = coincident + 1
    if coincident == 0:
        return 1

    weights = round(sum / coincident, 5)
    
    return weights
        





class Gene:
    def __init__(self):
        self.sink = 0
        self.source = 0
        self.weight = 0.0
        self.enabled = True
        self.innovation = 0


# class Neuron:
#     def __init__(self):
#         self.incoming = []
#         self.value = 0.0


def newInnovation():
    
    # Opening global modifiers from config file
    with open('C:\dog\dog\conf\global.json') as f:
        data = json.load(f)
    
    old_innovation = data["innovation"]
    new_innovation = int(old_innovation) + 1
    data["innovation"] = new_innovation
    
    with open('C:\dog\dog\conf\global.json', 'w') as json_file:
        json.dump(data, json_file)
    
    return new_innovation


if __name__ == "__main__":
    with open('C:\dog\dog\conf\global.json') as f:
        data = json.load(f)

    data["innovation"] = 4

    with open('C:\dog\dog\conf\global.json', 'w') as json_file:
        json.dump(data, json_file)