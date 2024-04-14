from sympy import parse_expr, Symbol, diff, solve, expand


class Operations:

    @staticmethod
    def calculateError(x, x0):

        if x == 0:
            return 0

        numerator = x - x0
        error = numerator / x
        absError = abs(error)
        return Operations.roundUp(absError, 6)

    @staticmethod
    def convergency(fx, crt):
        x = Operations.createSymbol("x")
        derivate = diff(fx, x)
        return -1 <= Operations.evaluateQuery(derivate, crt) <= 1

    @staticmethod
    def solveExpression(exp, symbol):
        return solve(exp, symbol)

    @staticmethod
    def expandExpression(exp):
        return expand(exp)

    @staticmethod
    def createSymbol(name):
        return Symbol(name)

    @staticmethod
    def parseExpression(exp):
        return parse_expr(exp)

    @staticmethod
    def evaluateQuery(query, numReplace):
        x = Operations.createSymbol("x")
        toEval = query.subs(x, numReplace).evalf()
        evaluatedQuery = float(toEval)
        return Operations.roundUp(evaluatedQuery, 4)

    @staticmethod
    def parsePercent(value):
        percent = value * 100
        return Operations.roundUp(percent, 4)

    @staticmethod
    def roundUp(value, n=2):
        multiplier = 10**n
        return round(value * multiplier) / multiplier
