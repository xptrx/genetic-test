#!/usr/bin/env python
import random


class Creature:
    def __init__(self, low, high, target, featuresNumber, features=[]):
        self.low = low
        self.high = high
        self.target = target
        self.featuresNumber = featuresNumber
        self.features = []
        if features == []:
            for i in range(featuresNumber):
                self.features.append(random.randint(low, high))
        else:
            self.features = features
        self.getFitness()

    def getFitness(self):
        self.fitness = abs(self.target - sum(self.features))

    def mutate(self, features):
        featureNumber = random.randint(0, self.featuresNumber - 1)
        features[featureNumber] = random.randint(self.low, self.high)
        # features[featureNumber] = random.randint(min(features),
        #                                          max(features))
        return features

    def crossOver(self, partner):
        halfSize = len(self.features) / 2
        childFeatures = []
        for i in range(len(self.features)):
            if 0.5 > random.random():
                childFeatures.append(self.features[i])
            else:
                childFeatures.append(partner.features[i])
        if 0.2 > random.random():
            childFeatures = self.mutate(childFeatures)
        return Creature(self.low,
                        self.high,
                        self.target,
                        self.featuresNumber,
                        childFeatures)

    def getAverageFitness(self):
        fitnessSum = sum([c.fitness for c in self.creatures])
        self.averageFitness = float(fitnessSum) / len(self.creatures)


class Population:
    def __init__(self, creatures_number, featuresNumber, low, high, target):
        self.creatures = []
        for i in range(creatures_number):
            self.creatures.append(Creature(low, high, target, featuresNumber))
        self.getAverageFitness()

    def getAverageFitness(self):
        fitnessSum = sum([c.fitness for c in self.creatures])
        self.averageFitness = float(fitnessSum) / len(self.creatures)

    def evolve(self):
        self.creatures.sort(key=lambda x: x.fitness)
        children = self.cross(2)
        self.creatures = children
        self.getAverageFitness()

    def cross(self, maxChildren):
        children = []
        childrenCount = 0
        for c, i in enumerate(self.creatures):
            for j in range(c, c+maxChildren):
                children.append(self.creatures[c].crossOver(self.creatures[j+1]))
                childrenCount += 1
                if childrenCount == len(self.creatures):
                    return children

    def show(self):
        print self.averageFitness
        for i in self.creatures:
            print i.features, i.fitness


if __name__ == "__main__":
    t = 200
    p = Population(10, 6, 0, 100, t)
    hist = []
    for i in range(100):
        p.evolve()
        hist.append( p.averageFitness)
    print "(Lower better)"
    print "Average: {0}".format(sum(hist)/len(hist))
    print "Best: {0}".format(min(hist))

