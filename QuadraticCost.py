import random
import math

import numpy as np

class QuadraticCost(object):
		def cost(a,y):
				return 0.5*np.linalg.norm(a-y)**2
		# error delta from output layer
		def delta(x,a,y):
				return (a-y) * sigmoid_prime(x)
