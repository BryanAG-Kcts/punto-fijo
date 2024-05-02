from customtkinter import CTkLabel
from .constants import DocConstants


class ImportantNotes:

    def init(root):
        CTkLabel(
            root,
            font=DocConstants.h1Size,
            text="NOTAS IMPORTANTES",
        ).pack()

        CTkLabel(
            root,
            text=
"""
Existe un error con la operación entre infinitos, pues el resultado es algo erróneo y se tiene que tomar en cuenta. Ejemplo: 1/log(0), log(0) si se toma individualmente, se evalúa correctamente, el resultado es infinito, pero cuando se realiza la división el resultado es 0. Lo cual es un inconveniente porque le da solución a ejercicios que en realidad no la tienen, o si la tienen, el resultado es otro.

Para evitar este problema puedes tomar valores más allá del limite de la función, es decir, adelantarse a la secuencia en las iteraciones, y escribir un número por debajo o por encima del limite

¿Como evitar este limite?. Para evitar este problema, evita escribir un valor inicial que no refleje una imagen en la función o muy cercanos a este
""",
            font=DocConstants.pSize,
            text_color="#aaa",
            justify="left",
            wraplength=900,
        ).pack(pady=10)
