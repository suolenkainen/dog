from src.player import Inputs, MaxNodes, Outputs
import src.utils as utils



class Network:
    def __init__(self):
        self.neurons = {}

class Neuron:
    def __init__(self):
        self.incoming = []
        self.value = 0.0

def generateNetwork(player):
    network = Network()

    for i in range(1, sum(Inputs)+1):
        network.neurons[i] = Neuron()

    for o in range(1,Outputs+1):
        network.neurons[MaxNodes+o] = Neuron()

    player.genes = sorted(player.genes, key=lambda x: x.source, reverse=False)

    for x in player.genes:
        print(x.source)

    for gene in player.genes:
        if gene.enabled:
            if gene.source not in network.neurons.keys():
                network.neurons[gene.source] = Neuron()
            neuron = network.neurons[gene.source]
            neuron.incoming.append(gene)
            if gene.sink not in network.neurons.keys():
                network.neurons[gene.sink] = Neuron()

    player.network = network



def evaluateCurrent(pool, deck):
    species = pool.species[pool.currentSpecies]
    player = species.players[pool.currentPlayer]

    inputs = getInputs(player, deck)
    output = evaluateNetwork(player.network, inputs)

    return output


def opponentCurrent(pool, deck):
    player = pool.opponent

    inputs = getInputs(player, deck)
    output = evaluateNetwork(player.network, inputs)

    return output


def evaluateNetwork(network, inputs):

    if len(network) == 0:
        return 3
    
    if len(inputs) != sum(Inputs):
        print("Incorrect number of neural network inputs.")
        return {}
	
    for i in range(sum(Inputs)):
        network.neurons[i+1].value = inputs[i]

    for neuron in network.neurons.values():
        temp_sum = 0
        for j in range(len(neuron.incoming)):
            incoming = neuron.incoming[j]
            other = network.neurons[incoming.sink]
            temp_sum = temp_sum + incoming.weight * other.value
		
        if neuron.incoming != []:
            neuron.value = utils.sigmoid(temp_sum)
	
    for o in range(Outputs):
        highest = [3,0]
        value = network.neurons[MaxNodes+o+1].value
        if value > highest[1]:
            highest = [o,value]
	
    return highest[0]


def getInputs(player, deck):    # Later add inputs like other cards in table, tiebreakers, etc.
    
    if len(player.hand) > 2:
        thirdcard = player.hand[2][0] + 104
    else:
        thirdcard = 209
    
    if len(player.hand) > 1:
        secondcard = player.hand[1][0] + 52
    else:
        secondcard = 209

    if len(player.hand) > 0:
        firstcard = player.hand[0][0]
    else:
        firstcard = 209
    
    


    tablehighest = -1
    for card in deck.table:
        (number, _), index = card
        if number > highest_card:
            highest_card = number
    if deck.table == []:
        tablehighest = 53
    
    tablehighest = tablehighest + 156

    triggers = [firstcard, secondcard, thirdcard, tablehighest]

    inputs = {}
    for x in range(sum(Inputs)):
        if x in triggers:
            inputs[x] = 1
        else:
            inputs[x] = 0

    return inputs