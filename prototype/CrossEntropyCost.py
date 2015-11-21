import random
import math

import numpy as np


class CrossEntropyCost(object):
    def cost(a, y):
        return np.sum(np.nan_to_num(-y * np.log(a) - (1 - y) * np.log(1 - a)))
    # error delta from output layer


    def delta(x, a, y):
        return (a - y)
