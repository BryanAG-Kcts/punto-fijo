from customtkinter import CTkFrame, CTkLabel
from components import firstValueInput, entryInput, errorInput
from services import operations

FirstValueInput = firstValueInput.FirstValueInput
EntryInput = entryInput.EntryInput
ErrorInput = errorInput.ErrorInput
Operations = operations.Operations


class Method:

    outputArea = None

    @staticmethod
    def setOutputArea(frame):
        Method.outputArea = frame

    @staticmethod
    def generateTable():

        frame = CTkFrame(Method.outputArea, corner_radius=10)
        frame.columnconfigure([0, 1, 2, 3], weight=1)

        headLabelN = CTkLabel(frame, text="n", fg_color="#4fa7eb")
        headLabelN.grid(row=0, column=0, sticky="nsew")

        headLabelX = CTkLabel(frame, text="X", fg_color="#4fa7eb")
        headLabelX.grid(row=0, column=1, sticky="nsew")

        headLabelGx = CTkLabel(frame, text="g(x)", fg_color="#4fa7eb")
        headLabelGx.grid(row=0, column=2, sticky="nsew")

        headLabelE = CTkLabel(frame, text="|eₐ|", fg_color="#4fa7eb")
        headLabelE.grid(row=0, column=3, sticky="nsew")

        n = 1
        x = float(FirstValueInput.getValue())
        fnGx = EntryInput.getValue()
        err = ErrorInput.getPercentValue()

        if fnGx.count("x") == 0:
            raise Exception("La función debe contener al menos una variable x")

        fnGx = Method.parseExpression(fnGx + "+ x")
        fnGx = Method.getFunctionValue(fnGx, x)

        while True:
            gx = Method.getFunctionValue(fnGx, x)
            e = Operations.calculateError(gx, x)
            e = Operations.parsePercent(e)
            print(f"n: {n}, x: {x}, g(x): {gx}, e: {e}")

            labelN = CTkLabel(frame, text=n)
            labelN.grid(row=n, column=0)

            labelX = CTkLabel(frame, text=x)
            labelX.grid(row=n, column=1)

            labelGx = CTkLabel(frame, text=gx)
            labelGx.grid(row=n, column=2)

            labelE = CTkLabel(frame, text=f"{e}%")
            labelE.grid(row=n, column=3)

            x = gx
            n += 1

            if e <= err:
                break

            convergency = Operations.convergency(fnGx, x)
            if convergency:
                raise Exception("La función no converge")

        return frame

    @staticmethod
    def getFunctionValue(gx, x):
        return Operations.evaluateQuery(gx, x)

    @staticmethod
    def parseExpression(gx):
        gx = gx.replace("^", "**")
        gx = gx.replace("π", "pi")
        gx = gx.replace("°", "*pi/180")
        # gx = gx.replace("e", "E")
        # gx = gx.replace("(", "((")
        # gx = gx.replace(")", "))")

        gx = gx.replace("²√", "sqrt")
        gx = gx.replace("√", "root")

        gx = gx.replace("sen(", "sin(")
        gx = gx.replace("cos(", "cos(")
        gx = gx.replace("tan(", "tan(")

        gx = gx.replace("csc(", "csc(")
        gx = gx.replace("sec(", "sec(")
        gx = gx.replace("cot(", "cot(")

        return gx
