from customtkinter import CTkLabel, CTkFrame
from documentation.constants import DocConstants


class UseGuide:

    guides = [
        {
            "title": "Input de entrada",
            "description": "Aquí insertarás tu función expresada en x. El sistema se encargará de hacer el despeje g(x). La función f(x) mínimo debe contener una variable x.",
        },
        {
            "title": "Valor inicial",
            "description": "Inserta el valor inicial de x, desde este punto empezaremos a iterar. Por lo que entre más cercano al cero, menos iteraciones se realizarán.",
        },
        {
            "title": "Error",
            "description": "Inserta en decimal el error permitido, el sistema se encargará de convertirlo a porcentaje, se dejará de iterar cuando el error aproximado actual sea menor o igual al mínimo permitido",
        },
    ]

    @staticmethod
    def init(root):
        CTkLabel(
            root,
            font=DocConstants.h1Size,
            text="GUÍA DE USO",
        ).pack()
        text = ""
        for guide in UseGuide.guides:
            title = guide["title"]
            desc = guide["description"]
            text += f"{title}: {desc}\n\n"

        CTkLabel(
            root,
            text=text,
            font=DocConstants.pSize,
            text_color="#aaa",
            justify="left",
            wraplength=900,
        ).pack(pady=10)
