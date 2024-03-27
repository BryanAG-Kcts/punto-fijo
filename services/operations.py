from math import *
from math import ceil


class Operations:

    @staticmethod
    def calculateError(x, x0):

        if x == 0:
            return 0

        numerator = x - x0
        error = numerator / x
        absError = abs(error)
        return Operations.roundUp(absError, 4)

    @staticmethod
    def evaluateQuery(query):
        evaluatedQuery = eval(query)
        return Operations.roundUp(evaluatedQuery, 4)

    @staticmethod
    def parsePercent(value):
        percent = value * 100
        return Operations.roundUp(percent, 4)

    @staticmethod
    def radical(value, n=2):
        return pow(value, 1 / n)

    @staticmethod
    def logAlias(value, n=10):
        return log(value, n)

    @staticmethod
    def roundUp(value, n=2):
        multiplier = 10**n
        return round(value * multiplier) / multiplier
