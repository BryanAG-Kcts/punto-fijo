from math import *
from math import ceil
from math import sqrt


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
    def radical(tuple):
        print(type(tuple))
        if type(tuple) is int or type(tuple) is float:
            return sqrt(tuple)

        value, n = tuple
        return pow(value, 1 / n)

    @staticmethod
    def logAlias(tuple):

        if type(tuple) is int or type(tuple) is float:
            return log(tuple)

        value, n = tuple
        return log(value, n)

    @staticmethod
    def roundUp(value, n=2):
        multiplier = 10**n
        return round(value * multiplier) / multiplier
