import random
import math

import numpy as np
import CrossEntropyCost as cecost
import Quadratic Cost as qcost


class NeuralNet(object):
    def __init__(self, layers, cost = cecost):

        self.layers = len(layers)
        self.neurons_in_layer = layers
        self.bias = [np.random.randn(x, 1) for x in layers[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(layers[:-1], layers[1:])]
        self.cost = cost

    def feed(self, x):

        act = x
        acts = [x]
        zv = []
        for b, w in zip(self.bias, self.weights):
            z = np.dot(w, act) + b
            act = self.sigmoid(z)
            acts.append(act)
        return acts[-1]

    def train(self, minibatch_s, train_set, learn_rate, epoch, lmbda = 0.0):

        for e in xrange(epoch):
            random.shuffle(train_set)
            minibatches = [train_set[k:k + minibatch_s] for k in xrange(0, len(train_set), minibatch_s)]
            for mini_batch in minibatches:
                self.update(learn_rate, minibatch_s, mini_batch, lmbda)
                # s= str(eval(minibatch))
                # print s
            print e
            # for w,b in zip(self.weights,self.bias):
            #    print "bias",b
            #   print "weights",w

    def update(self, learn_rate, minibatch_size, mini_batch, lmbda):

        nb = [np.zeros(b.shape) for b in self.bias]
        nw = [np.zeros(w.shape) for w in self.weights]
        # print nw
        for x, y in mini_batch:
            nweights, nbias = self.back_prop(x, y)
            # print nweights
            # print zip(nweights,nw)
            # print "-------------------------------------"
            # print self.weights
            nw = [a + aa for a, aa in zip(nweights, nw)]
            nb = [b + bb for b, bb in zip(nbias, nb)]
        #                    print self.weights
        # print nw

        rate = learn_rate / minibatch_size

        self.weights = [(1-eta*(lmbda/n)) * sw - rate * n for sw, n in zip(self.weights, nw)]
        self.bias = [sb - rate2 * b for sb, b in zip(self.bias, nb)]

    def back_prop(self, input, output):
        # print input
        nweights = [np.zeros(w.shape) for w in self.weights]
        nbias = [np.zeros(b.shape) for b in self.bias]

        activation = np.array(input)
        activations = [activation]
        zv = []

        for b, w in zip(self.bias, self.weights):
            z = np.dot(w, activation) + b
            zv.append(z)
            activation = self.sigmoid(z)
            activations.append(activation)
        #                print zv
        #                print activations
        output = np.array(output)
        delta = (self.cost).delta(zv[-1], activations[-1], output)

        #                print activations[-2].transpose()
        #                print delta
        # print activations[-2].shape
        # print delta.shape
        nweights[-1] = np.dot(delta, activations[-2].transpose())
        nbias[-1] = delta
        ds = [delta]

        # xrange?
        for l in range(2, self.layers):
            m = np.dot(self.weights[-l + 1].transpose(), delta)
            n = self.sigmoidpr(zv[-l])
            delta = np.multiply(m, n)
            ds.append(delta)
            # print delta
            # print activations[-l-1]
            nweights[-l] = np.dot(delta, activations[-l - 1].transpose())
            nbias[-l] = delta
        #                print nweights
        return (nweights, nbias)

    def eval(self, inp):
        perc = []
        for i, x in inp:
            res = self.feed(inp)
            perc.append((x - out) / x)
        err = sum(perc) / len(perc)
        return err

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoidpr(self, x):
        return (1 - self.sigmoid(x)) * (self.sigmoid(x))


from read import getData as gd

if __name__ == '__main__':
    g = gd()
    train_data = g.get_trainset(0.8)
    n = NeuralNet([266, 100, 100, 2])
    n.train(10, train_data, 0.001, 1000)
