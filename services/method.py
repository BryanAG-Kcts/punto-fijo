from customtkinter import CTkFrame, CTkLabel
from components import firstValueInput, entryInput, errorInput
from services import operations
from re import sub

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

        fnGx = "x + " + fnGx

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

            if n > 100:
                raise Exception(
                    "La función no converge (Se hicieron más de 100 iteraciones). Disminuye el porcentaje de error o dar un valor inicial más cercano"
                )
                break

        return frame

    @staticmethod
    def getFunctionValue(gx, x):
        gx = gx.replace("^", "**")
        gx = gx.replace("π", "pi")
        gx = gx.replace("e", "E")
        gx = gx.replace("(", "((")
        gx = gx.replace(")", "))")

        gx = gx.replace("√", "Operations.radical")
        gx = sub(r"\|([^|]+)\|", "abs(\\1)", gx)

        gx = gx.replace("sen(", "sin(rad")
        gx = gx.replace("cos(", "cos(rad")
        gx = gx.replace("tan(", "tan(rad")

        gx = gx.replace("csc(", "csc(rad")
        gx = gx.replace("sec(", "sec(rad")
        gx = gx.replace("cot(", "cot(rad")
        return Operations.evaluateQuery(gx, x)
