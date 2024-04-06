from sympy import *


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
    def evaluateQuery(query, numReplace):
        x = Symbol("x")
        func = parse_expr(query, evaluate=False)
        evaluatedQuery = func.subs(x, numReplace).evalf()
        print(evaluatedQuery)
        return Operations.roundUp(evaluatedQuery, 4)

    @staticmethod
    def parsePercent(value):
        percent = value * 100
        return Operations.roundUp(percent, 4)

    @staticmethod
    def roundUp(value, n=2):
        multiplier = 10**n
        return round(value * multiplier) / multiplier
