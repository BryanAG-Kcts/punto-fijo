from customtkinter import CTkLabel
from documentation.constants import DocConstants


class MathFunctions:
    functions = [
        {
            "title": "Exponente",
            "description": "Puedes usar ^ o **",
        },
        {
            "title": "Euler",
            "description": "Puedes usar E",
        },
        {
            "title": "Número π",
            "description": "Puedes usar π o pi",
        },
        {
            "title": "Radicando",
            "description": "Puedes usar √(exp, rad) o root(exp, rad). Para una raíz cuadrada puedes usar ²√()",
        },
        {
            "title": "seno",
            "description": "Puedes usar sen(rad) o sin(rad)",
        },
        {
            "title": "coseno",
            "description": "Puedes usar cos(rad)",
        },
        {
            "title": "tangente",
            "description": "Puedes usar tan(rad)",
        },
        {
            "title": "cosecante",
            "description": "Puedes usar csc(rad)",
        },
        {
            "title": "secante",
            "description": "Puedes usar sec(rad)",
        },
        {
            "title": "cotangente",
            "description": "Puedes usar cot(rad)",
        },
        {
            "title": "logaritmo",
            "description": "Puedes usar log(x, base) para calcular cualquier logaritmo. Usa ln(x) o log(x) para calcular logaritmos naturales.",
        },
        {
            "title": "Radianes",
            "description": "Puedes usar ° para convertir grados a radianes. Por defecto, las funciones trigonométricas trabajan con radianes, por lo que es necesario una transformación si necesitas usar grados. Ejemplo, tan(90) = -1.9952 mientras que tan(90°) es indeterminado",
        },
        {
            "title": "Euler exponencial",
            "description": "Puedes usar exp(x) o E^x",
        },{
            "title": "Extras",
            "description": "Puedes usar cualquier función soportada por Sympy (librería de Python). Puedes revisar su documentación oficial para enterarte de más funciones",
        },
    ]

    @staticmethod
    def init(root):
        CTkLabel(
            root,
            font=DocConstants.h1Size,
            text="FUNCIONES PERMITIDAS",
        ).pack()
        text = ""
        for guide in MathFunctions.functions:
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
