# write neurons and connections
import json
import src.species as spc
import src.player as plr
import src.utils as utils

class Pool:
    def __init__(self):
        self.species = []
        self.opponent = self.createOpponen()
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
        
    
    def createOpponen(self):
        self.opponent = plr.Player()
        self.opponent.index = -1
        self.opponent.seed = -1
        self.opponent.mutatePlayer()


    def addToSpecies(self, child):

        confs = {}
        confs["DeltaDisjoint"] = self.DeltaDisjoint
        confs["DeltaWeights"] = self.DeltaWeights
        confs["DeltaThreshold"] = self.DeltaThreshold

        foundSpecies = False
        for species in self.species:
            if utils.sameSpecies(confs, child, species.players[0]):
                species.players.append(child)
                foundSpecies = True
                break
        
        if not foundSpecies:
            childSpecies = spc.Species()
            childSpecies.players.append(child)
            self.species.append(childSpecies)




if __name__ == "__main__":
    with open('C:\dog\dog\conf\global.json') as f:
        data = json.load(f)

    data["innovation"] = 4

    with open('C:\dog\dog\conf\global.json', 'w') as json_file:
        json.dump(data, json_file)