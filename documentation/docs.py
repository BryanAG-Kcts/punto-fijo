from customtkinter import CTkScrollableFrame, CTkLabel
from services.method import Method
from components.entryInput import EntryInput
from components.output import Output
from .constants import DocConstants
from .useGuide import UseGuide
from .mathFunctions import MathFunctions
from .important import ImportantNotes


class Docs:

    @staticmethod
    def init(root):

        frame = CTkScrollableFrame(root, fg_color="#e0e0e0")
        frame.pack(fill="both", expand=True, side="left", padx=20)

        CTkLabel(
            frame,
            font=DocConstants.h1Size,
            text="MÉTODO DE PUNTO FIJO",
        ).pack()

        CTkLabel(
            frame,
            font=DocConstants.h2Size,
            text="Bryan David Álvarez Galvis 192096",
            text_color="#bbb",
        ).pack()

        CTkLabel(
            frame,
            font=DocConstants.pSize,
            text="""
El método de punto fijo es un método iterativo de carácter abierto, usado en análisis numérico para encontrar una solución aproximada a una ecuación f(x)=0.

La idea de este método es de transformar la ecuación original en una forma equivalente g(x)=x, donde estaremos iterando desde un valor inicial hasta llegar a una imagen con un valor aproximado de cero. Es decir, hallamos recursivamente los siguientes valores que tomara g(x) a partir del resultado previamente obtenido xₙ = g(xₙ₋₁).

Para poder confirmar si g(x) eventualmente converge a cero, evaluamos la primera derivada de g(x), si esta es menor o igual a 1, podemos continuar, caso contrario, la función diverge y no tiene caso seguir iterando. Por ejemplo, tomemos como f(x) = E^(-x) - x, por lo que despejando x tenemos como g(x), x = E^(-x). La línea roja representa g(x), mientras que la línea azul representa y = x, y por ultimo, la linea verde representa el puto común entre g(x) y y = x

No todos los despejes de x nos llevarán a una aproximación de la respuesta, según el criterio de convergencia, el valor absoluto de la imagen de la derivada de g(x) debe ser menor o igual a 1, sino no convergerá""",
            text_color="#aaa",
            justify="left",
            wraplength=900,
        ).pack(pady=20)

        Method.setOutputArea(frame)
        EntryInput.handleEntryValue("-x + E^(-x)")
        Output.print()
        EntryInput.clear()
        UseGuide.init(frame)
        MathFunctions.init(frame)
        ImportantNotes.init(frame)
