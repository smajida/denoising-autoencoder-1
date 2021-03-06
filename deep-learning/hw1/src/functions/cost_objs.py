import numpy as np


class QuadraticCost:
    @staticmethod
    def function(y, z):
        return 0.5 * np.sum((z - y) ** 2, axis=1)

    @staticmethod
    def derivative(y, z):
        return z - y


class CrossEntropyCost:
    @staticmethod
    def function(y, z):
        return -np.sum(y * np.log(z) + (1 - y) * np.log(1 - z))/np.float64(y.shape[0])

    @staticmethod
    def derivative(y, z):
        return (z - y) / ((z + 1) * z)


class MulticlassCrossEntropyCost:
    @staticmethod
    def function(y, z):
        return -np.sum(np.sum(y * np.log(z)))/np.float64(y.shape[0])

    @staticmethod
    def derivative(y, z):
        return z - y
