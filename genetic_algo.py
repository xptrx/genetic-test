#!/usr/bin/env python
import random


class Creature:
    def __init__(self, low, high, target, featuresNumber,
                 features=[],
                 mutationChance=0.2):
        self.low = low
        self.high = high
        self.target = target
        self.featuresNumber = featuresNumber
        self.mutationChance = mutationChance
        if features == []:
            self.features = []
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
        childFeatures = []
        for i in range(len(self.features)):
            if 0.5 > random.random():
                childFeatures.append(self.features[i])
            else:
                childFeatures.append(partner.features[i])
        if self.mutationChance > random.random():
            childFeatures = self.mutate(childFeatures)
        return Creature(self.low,
                        self.high,
                        self.target,
                        self.featuresNumber,
                        childFeatures)


class Population:
    def __init__(self, low, high, target, featuresNumber, creatures_number):
        self.creatures = []
        self.generation = 0
        for i in range(creatures_number):
            self.creatures.append(Creature(low, high, target, featuresNumber))
        self.getAverageFitness()

    def getAverageFitness(self):
        fitnessSum = sum([c.fitness for c in self.creatures])
        self.averageFitness = float(fitnessSum) / len(self.creatures)

    def evolve(self):
        self.generation += 1
        self.creatures.sort(key=lambda x: x.fitness)
        children = self.cross(2)
        self.creatures = children
        self.getAverageFitness()

    def cross(self, maxChildren):
        children = []
        childrenCount = 0
        for c, i in enumerate(self.creatures):
            for j in range(c, c+maxChildren):
                child = self.creatures[c].crossOver(self.creatures[j+1])
                children.append(child)
                childrenCount += 1
                if childrenCount == len(self.creatures):
                    return children

    def show(self):
        print self.averageFitness
        for i in self.creatures:
            print i.features, i.fitness

    def check(self):
        for i in self.creatures:
            if i.fitness == 0.0:
                return (True, self.generation, i.features)
        return (False, self.generation, [])
