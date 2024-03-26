from customtkinter import CTkFrame, CTkLabel
from components import firstValueInput, entryInput, errorInput
from services import operations

FirstValueInput = firstValueInput.FirstValueInput
EntryInput = entryInput.EntryInput
ErrorInput = errorInput.ErrorInput
Operations = operations.Operations


class Method:

    @staticmethod
    def generateTable():

        frame = CTkFrame(None)
        frame.columnconfigure([0, 1, 2, 3], weight=1)

        headLabelN = CTkLabel(frame, text="n")
        headLabelN.grid(row=0, column=0)

        headLabelX = CTkLabel(frame, text="X")
        headLabelX.grid(row=0, column=1)

        headLabelGx = CTkLabel(frame, text="g(x)")
        headLabelGx.grid(row=0, column=2)

        headLabelE = CTkLabel(frame, text="|e|")
        headLabelE.grid(row=0, column=3)

        n = 0
        x = float(FirstValueInput.getValue())
        fnGx = EntryInput.getValue()
        err = ErrorInput.getPercentValue()

        while True:

            gx = Method.getFunctionValue(fnGx, x)
            e = Operations.calculateError(gx, x)
            e = Operations.parsePercent(e)

            print(f"n: {n}, x: {x}, g(x): {gx}, e: {e}")

            labelN = CTkLabel(frame, text=n)
            labelN.grid(row=n + 1, column=0)

            labelX = CTkLabel(frame, text=x)
            labelX.grid(row=n + 1, column=1)

            labelGx = CTkLabel(frame, text=gx)
            labelGx.grid(row=n + 1, column=2)

            labelE = CTkLabel(frame, text=f"{e}%")
            labelE.grid(row=n + 1, column=3)

            x = gx
            n += 1

            if e <= err:
                break

        return frame

    @staticmethod
    def getFunctionValue(gx, x):
        gx = gx.replace("x", str(x))
        gx = gx.replace("^", "**")
        return Operations.evaluateQuery(gx)
