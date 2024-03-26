from math import *


class Operations:

    @staticmethod
    def calculateError(x, x0):
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
        percent = value * 100
        return round(percent, 4)
