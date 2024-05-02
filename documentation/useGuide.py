from customtkinter import CTkLabel
from documentation.constants import DocConstants


class UseGuide:

    guides = [
        {
            "title": "Input de entrada",
            "description": "Aquí insertarás tu función expresada en x, no f(x) = 0, introduce en este input netamente la función. El sistema se encargará de hacer el despeje g(x). La función f(x) mínimo debe contener una variable xm puedes apoyarte con el panel numérico de la parte inferior. No hay valor por defecto. Si la función de entrada tiene un fácil despeje, el sistema mostrará el primer valor resultante que cumpla con f(x) = 0",
        },
        {
            "title": "Valor inicial",
            "description": "Inserta el valor inicial de x, desde este punto empezaremos a iterar. Por lo que entre más cercano al cero de la función, menos iteraciones se realizarán. Valor por defecto = 0",
        },
        {
            "title": "Error",
            "description": "Inserta en decimal el error permitido, el sistema se encargará de convertirlo a porcentaje, se dejará de iterar cuando el error aproximado actual sea menor o igual al mínimo permitido. Valor por defecto = 0.01, es decir, 1%",
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
