from math import *


class Operations:

    @staticmethod
    def calculateError(x, x0):

        if x == 0:
            return 0

        numerator = x - x0
        error = numerator / x
        absError = abs(error)
        return round(absError, 4)

    @staticmethod
    def evaluateQuery(query):
        evaluatedQuery = eval(query)
        return round(evaluatedQuery, 4)

    @staticmethod
    def parsePercent(value):
        print(value)
        percent = value * 100
        return percent
