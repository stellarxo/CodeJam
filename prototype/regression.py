import random
import math

import numpy as np

class RegModel(object):
    def __init__(self, feature_size):
        self.parameters = np.random.randn(feature_size + 1, 1)
        self.old_parameters = np.zeros(self.parameters.shape)
        self.cost = 100

    def train(self, train_set, eta):
        random.shuffle(train_set)
        while self.cost_func(train_set) > 0.00000000001:
            for y, x in train_set:
                x = np.insert(x, 0, 1)
                self.update(eta, y, x)
            # print self.cost_func(train_set)

            # print self.parameters

    def update(self, eta, output, input):
        newp = np.zeros(self.parameters.shape)
        for j in xrange(len(input)):
            newp = eta * (self.cost_derivative(input, output) * input[j])
            self.old_parameters[j] = self.parameters[j]
            self.parameters[j] = self.parameters[j] + newp

    def cost_derivative(self, x, y):
        return (y - self.reg(x))

    def cost_func(self, train_set):
        suma = []
        for y, x in train_set:
            x = np.insert(x, 0, 1)
            a = 1.0 / 2.0 * (y - self.reg(x)) ** 2
            suma.append(a)
        sum = np.sum(suma)
        return 1.0 / len(train_set) * sum

    def reg(self, x):
        output = np.dot(self.parameters.transpose(), x)
        # print output
        return output
