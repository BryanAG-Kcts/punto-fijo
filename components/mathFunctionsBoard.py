from customtkinter import CTkFrame, CTkButton
from components import entryInput

EntryInput = entryInput.EntryInput

mathFunctions = [
    {"name": "euler", "value": "E"},
    {"name": "exponente", "value": "^"},
    {"name": "π", "value": "π"},
    {"name": "()", "value": "( )"},
    {"name": "x²", "value": "x^2"},
    {"name": "E^x", "value": "E^x"},
    {"name": "√", "value": "√(x, rad)"},
    {"name": "²√x", "value": "²√(x)"},
    {"name": "seno", "value": "sen(x)"},
    {"name": "coseno", "value": "cos(x)"},
    {"name": "tangente", "value": "tan(x)"},
    {"name": "cosecante", "value": "csc(x)"},
    {"name": "secante", "value": "sec(x)"},
    {"name": "cotangente", "value": "cot(x)"},
    {"name": "ln", "value": "ln(x)"},
    {"name": "log", "value": "log(x, base)"},
    {"name": "radianes", "value": "°"},
]


class MathFunctionsBoard:

    @staticmethod
    def handleClick(value):
        EntryInput.handleEntryValue(value)

    @staticmethod
    def init(root):
        row = 0
        col = 0

        frame = CTkFrame(root)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure([0, 1, 2, 3, 4, 5], weight=1)

        for mathFunction in mathFunctions:
            button = CTkButton(
                frame,
                text=mathFunction["name"],
                command=lambda x=mathFunction["value"]: MathFunctionsBoard.handleClick(
                    x
                ),
                height=70,
                fg_color="#C7C7C7",
                hover_color="#bbb",
                font=("Arial", 20),
                text_color="#000",
            )
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            col = col + 1 if col < 5 else 0
            row = row + 1 if col == 0 else row
