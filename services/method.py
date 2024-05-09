from customtkinter import CTkFrame, CTkLabel
from components import firstValueInput, entryInput, errorInput
from services import operations, graphic

FirstValueInput = firstValueInput.FirstValueInput
EntryInput = entryInput.EntryInput
ErrorInput = errorInput.ErrorInput
Operations = operations.Operations
Graphic = graphic.Graphic


class Method:

    outputArea = None

    @staticmethod
    def setOutputArea(frame):
        Method.outputArea = frame

    @staticmethod
    def calculateGx():
        x = float(FirstValueInput.getValue())
        fnGx = EntryInput.getValue()
        fnGx = Method.parseExpression(fnGx)
        err = ErrorInput.getPercentValue()
        y = Operations.createSymbol("y")
        continueAttempt = True

        # Si no tiene x la expresión, detener el proceso
        if fnGx.count("y") != 0:
            raise Exception(
                "La variable 'y' está reservada. Recuerda, f(x) debe estar en función de x"
            )

        if fnGx.count("x") == 0:
            raise Exception("La función debe contener al menos una variable x")

        # Recorro cada carácter de la expresión para interceptar las x y cambiarlas por y. Esto con el fin de poder despejar la función
        iterations = len(fnGx)
        i = 0
        while i < iterations:
            toReplace = [*fnGx]
            if toReplace[i] == "x":
                toReplace[i] = "y"
                fnY = "".join(toReplace)
                print(fnY)
                gx = Operations.solveExpression(fnY, y)
                # Recorro los posibles despejes de gx
                for j in range(len(gx)):
                    try:
                        response = Method.generateTable(x, gx[j], err)
                        if response[0]:

                            _, frame, rows, xf = response

                            plotter = Graphic.generateGraphic(
                                frame,
                                gx[j],
                                rows,
                                float(xf),
                            )
                            return [response[1], plotter]
                    except:
                        pass

            if (i == len(fnGx) - 1) and continueAttempt:
                print("a")
                continueAttempt = False
                fnGx = "(" + fnGx + ") + x"
                iterations = len(fnGx)
                i = -1

            i += 1

        # Lanzar excepción si ningún despeje converge
        raise Exception("No se pudo encontrar una solución, la función no converge")

    @staticmethod
    def generateTable(x, fnGx, err):
        frame = CTkFrame(Method.outputArea, corner_radius=10)
        frame.columnconfigure([0, 1, 2, 3], weight=1)

        headLabelN = CTkLabel(frame, text="n", fg_color="#4fa7eb")
        headLabelN.grid(row=0, column=0, sticky="nsew")

        headLabelX = CTkLabel(frame, text="x", fg_color="#4fa7eb")
        headLabelX.grid(row=0, column=1, sticky="nsew")

        headLabelGx = CTkLabel(frame, text=f"x = {fnGx}", fg_color="#4fa7eb")
        headLabelGx.grid(row=0, column=2, sticky="nsew")

        headLabelE = CTkLabel(frame, text="|eₐ|", fg_color="#4fa7eb")
        headLabelE.grid(row=0, column=3, sticky="nsew")

        n = 1
        while True:
            gx = Method.getFunctionValue(fnGx, x)
            e = Operations.calculateError(gx, x)
            e = Operations.parsePercent(e)
            color = "#dbdbdb" if n % 2 == 0 else "#e0e0e0"

            labelN = CTkLabel(frame, text=n, fg_color=color)
            labelN.grid(row=n, column=0, sticky="nsew")

            labelX = CTkLabel(frame, text=f"{x:.4f}", fg_color=color)
            labelX.grid(row=n, column=1, sticky="nsew")

            labelGx = CTkLabel(frame, text=f"{gx:.4f}", fg_color=color)
            labelGx.grid(row=n, column=2, sticky="nsew")

            labelE = CTkLabel(frame, text=f"{e:.4f}%", fg_color=color)
            labelE.grid(row=n, column=3, sticky="nsew")

            x = gx
            n += 1

            # Si el error actual es menor o igual al solicitado, romper ciclo
            if e <= err:
                break

            # Si el remplazo de xi en g'(x) es mayor que 1 o menor que -1, significa que el despeje con converge
            convergency = Operations.convergency(fnGx, x)
            if not convergency:
                return [False]

        # Error, frame a renderizar, número de iteraciones, valor aproximado del cero
        CTkLabel(
            frame,
            text=f"El valor aproximado del cero de la función, para un error de {err:.4f}% es de {x}",
        ).grid(row=n + 1, column=0, sticky="nsew", columnspan=4)
        return [True, frame, n, x]

    @staticmethod
    def getFunctionValue(gx, x):
        return Operations.evaluateQuery(gx, x)

    @staticmethod
    def parseExpression(gx):
        # Reemplazar caracteres especiales por sus equivalentes en Python
        gx = gx.replace("^", "**")
        gx = gx.replace("π", "pi")
        gx = gx.replace("°", "*pi/180")
        gx = gx.replace("²√", "sqrt")
        gx = gx.replace("√", "root")
        gx = gx.replace("sen(", "sin(")
        gx = gx.replace("cos(", "cos(")
        gx = gx.replace("tan(", "tan(")
        gx = gx.replace("csc(", "csc(")
        gx = gx.replace("sec(", "sec(")
        gx = gx.replace("cot(", "cot(")

        return gx
