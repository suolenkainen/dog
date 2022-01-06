# write neurons and connections
import json

class Pool:
    def __init__(self):
        self.species = {}
        self.generation = 0
        self.innovation = 4
        self.currentSpecies = 1
        self.currentGenome = 1
        self.currentFrame = 0
        self.maxFitness = 0
    
    def newInnovation(self):
        self.innovation = self.innovation + 1
        return self.innovation


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