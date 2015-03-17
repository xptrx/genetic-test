#!/usr/bin/env python
import random


class BruteForce:
    def __init__(self, low, high, target, featuresNumber):
        self.low = low
        self.high = high
        self.target = target
        self.featuresNumber = featuresNumber

    def run(self):
        generations = 0
        while True:
            features = []
            generations += 1
            for i in range(self.featuresNumber):
                features.append(random.randint(self.low, self.high))
            if sum(features) == self.target:
                return (generations, features)
