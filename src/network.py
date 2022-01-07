from src.player import Inputs, MaxNodes, Outputs


class Network:
    def __init__(self):
        self.neurons = {}

class Neuron:
    def __init__(self):
        self.incoming = []
        self.value = 0.0

def generateNetwork(player):
    network = Network()

    for i in range(1, Inputs+1):
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



def evaluateCurrent(pool):
	species = pool.species[pool.currentSpecies]
	player = species.players[pool.currentplayer]

	inputs = getInputs()
	controller = evaluateNetwork(player.network, inputs)


# def evaluateNetwork(network, inputs):
# 	table.insert(inputs, 1)
# 	if #inputs ~= Inputs then
# 		console.writeline("Incorrect number of neural network inputs.")
# 		return {}
# 	end
	
# 	for i=1,Inputs do
# 		network.neurons[i].value = inputs[i]
# 	end
	
# 	for _,neuron in pairs(network.neurons) do
# 		local sum = 0
# 		for j = 1,#neuron.incoming do
# 			local incoming = neuron.incoming[j]
# 			local other = network.neurons[incoming.into]
# 			sum = sum + incoming.weight * other.value
# 		end
		
# 		if #neuron.incoming > 0 then
# 			neuron.value = sigmoid(sum)
# 		end
# 	end
	
# 	local outputs = {}
# 	for o=1,Outputs do
# 		local button = "P1 " .. ButtonNames[o]
# 		if network.neurons[MaxNodes+o].value > 0 then
# 			outputs[button] = true
# 		else
# 			outputs[button] = false
# 		end
# 	end
	
# 	return outputs
# end