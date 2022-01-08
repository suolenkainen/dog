import random
import src.pool as gn
import src.utils as utils

Inputs = [52, 52, 52, 53, 2]
Outputs = 4 # 0,1,2 are hand cards while 3 is a deck card
MaxNodes= 1000000

class Player:
    def __init__(self):
        # Creating a player that functions as a genome in evolution
        # The player has basic player values and starting mutation rates (moved to conf-file?)
        self.index = -1
        self.hand = []
        self.stash = []
        self.score = -10
        self.seed = 0
        self.inputs = sum(Inputs)
        self.next = True
        
        MutateConnectionsChance = 0.25
        LinkMutationChance = 2.0
        NodeMutationChance = 0.50
        BiasMutationChance = 0.40
        StepSize = 0.1
        DisableMutationChance = 0.4
        EnableMutationChance = 0.2

        # Player has characteristics that enable the use of genes as part of evolution
        # These enable the use of evolution networks and ranking the players
        self.genes = []
        self.fitness = 0
        self.adjustedFitness = 0
        self.network = {}
        self.maxneuron = sum(Inputs)
        self.globalRank = 0
        self.mutationRates = {}
        self.mutationRates["connections"] = MutateConnectionsChance
        self.mutationRates["link"] = LinkMutationChance
        self.mutationRates["bias"] = BiasMutationChance
        self.mutationRates["node"] = NodeMutationChance
        self.mutationRates["enable"] = EnableMutationChance
        self.mutationRates["disable"] = DisableMutationChance
        self.mutationRates["step"] = StepSize

            
    def mutatePlayer(self):
        #This function acts as a prompt for starting a mutation of each kind
        
        random.seed(self.seed)
        
        #at each mutation phase the rates are slightly changed to accommodate new variation in genes
        for mutation, rate in self.mutationRates.items():
            if random.choice([1,2]) == 1:
                self.mutationRates[mutation] = round(0.95*rate, 5)
            else:
                self.mutationRates[mutation] = round(1.05263*rate, 5)

        # This mutation mutates the genes' weight slightly
        if random.random() < self.mutationRates["connections"]:
            self.pointMutate()
        
        # This mutation generates two new neurons and generates a link between them
        # This is essentially the way to generate new genes to a gene pool
        lr = self.mutationRates["link"]
        while lr > 0:
            if random.random() < lr:
                self.linkMutate(False)
            lr = lr - 1

        # This generates a bias link to a certain output node
        # It receives an input from all input nodes
        br = self.mutationRates["bias"]
        while br > 0:
            if random.random() < br:
                self.linkMutate(True)
            br = br - 1
        
        # This disables one gene and generates two new genes in its stead.
        # These are both new innovations compared to the old gene
        nr = self.mutationRates["node"]
        while nr > 0:
            if random.random() < nr:
                self.nodeMutate()
            nr = nr - 1
        
        # This chooses random disabled gene and enables it
        er = self.mutationRates["enable"]
        while er > 0:
            if random.random() < er:
                self.enableDisableMutate(True)
            er = er - 1

        # This chooses random enabled gene and disables it
        dr = self.mutationRates["disable"]
        while dr > 0:
            if random.random() < dr:
                self.enableDisableMutate(False)
            dr = dr - 1


    def pointMutate(self):
        # Mutate the weight of the gene using steps. Round the weight to 5 decimals
        
        random.seed(self.seed)
        PerturbChance = 0.90
        step = self.mutationRates["step"]
        
        for gene in self.genes:
            if random.random() < PerturbChance:
                gene.weight = round(gene.weight + random.random() * step*2 - step, 5)
            else:
                gene.weight = round(random.random()*4-2, 5)


    
    def linkMutate(self, forceBias):
        # Generate a new link between nodes if there exists none yet
        # This essentially generates new genes

        random.seed(self.seed)

        neuron1 = self.randomNeuron(False)
        neuron2 = self.randomNeuron(True)
        
        newLink = Gene()
        if neuron1 <= sum(Inputs) and neuron2 <= sum(Inputs):
            # Both input nodes
            return

        if neuron2 <= sum(Inputs):
            # Swap output and input
            temp = neuron1
            neuron1 = neuron2
            neuron2 = temp

        newLink.sink = neuron1
        newLink.source = neuron2
        if forceBias:
            newLink.sink = sum(Inputs)
        
        if self.containsLink(newLink):
            return

        newLink.innovation = utils.newInnovation()
        newLink.weight = round(random.random()*4-2, 5)
        
        self.genes.append(newLink)

    
    def nodeMutate(self):
        # This generates a new node between two existing nodes that had connections

        random.seed(self.seed)
        if self.genes == []:
            return

        self.maxneuron = self.maxneuron + 1

        gene = random.choice(self.genes)
        if not gene.enabled:
            return

        gene.enabled = False
        
        gene1 = self.copyGene(gene)
        gene1.source = self.maxneuron
        gene1.weight = 1.0
        gene1.innovation = utils.newInnovation()
        gene1.enabled = True
        self.genes.append(gene1)
        
        gene2 = self.copyGene(gene)
        gene2.sink = self.maxneuron
        gene2.innovation = utils.newInnovation()
        gene2.enabled = True
        self.genes.append(gene2)

    
    def enableDisableMutate(self, enable):
        #This chooses one gene and switches it to enabled or disabled

        random.seed(self.seed)

        candidates = []
        for gene in self.genes:
            if gene.enabled != enable:
                candidates.append(gene)
	
        if candidates == []:
            return
            
        gene = random.choice(candidates)
        gene.enabled = not gene.enabled



    def randomNeuron(self, nonInput):
        # Choose any neuron that are existing by default (Inputs and Outputs) and
        # from those that are already existing in genes

        random.seed(self.seed)
        
        m = MaxNodes +1
        neurons = list(range(m, m+Outputs))

        if not nonInput:
            neurons += list(range(1, sum(Inputs)+1))
        
        for gene in self.genes:
            if (not nonInput) or gene.sink > sum(Inputs):
                neurons.append(gene.sink)
            if (not nonInput) or gene.source > sum(Inputs):
                neurons.append(gene.source)

        return neurons[random.randint(0,len(neurons)-1)]


    def containsLink(self, link):
        # Checks if a link already exists in other genes
        for gene in self.genes:
            if gene.sink == link.sink and gene.source == link.source:
                return True
    
    def copyGene(self, gene):
        # Copies a gene
        local_gene = Gene()
        local_gene.sink = gene.sink
        local_gene.source = gene.source
        local_gene.weight = gene.weight
        local_gene.enabled = gene.enabled
        local_gene.innovation = gene.innovation
        return local_gene


class Gene:
    def __init__(self):
        self.sink = 0
        self.source = 0
        self.weight = 0.0
        self.enabled = True
        self.innovation = 0