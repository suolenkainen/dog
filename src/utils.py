import json
import math 


def sameSpecies(confs, player1, player2):
    dd = confs["DeltaDisjoint"]*disjoint(player1.genes, player2.genes)
    dw = confs["DeltaWeights"]*weights(player1.genes, player2.genes) 
    return dd + dw < confs["DeltaThreshold"]


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


def sigmoid(x):

    if x == 0:
        return 0

    result = 2 / (1 + math.log(4.9 * x)) - 1

    return result
