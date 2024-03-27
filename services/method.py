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

        headLabelE = CTkLabel(frame, text="|e|", fg_color="#4fa7eb")
        headLabelE.grid(row=0, column=3, sticky="nsew")

        n = 1
        x = float(FirstValueInput.getValue())
        fnGx = EntryInput.getValue()
        err = ErrorInput.getPercentValue()

        if fnGx.count("x") == 0:
            raise Exception("La función debe contener al menos una variable x")

        fnGx += " + x "

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

        return frame

    @staticmethod
    def getFunctionValue(gx, x):
        gx = gx.replace("x", f"({x})")
        gx = gx.replace("^", "**")
        return Operations.evaluateQuery(gx)
