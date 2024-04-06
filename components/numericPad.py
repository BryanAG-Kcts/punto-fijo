from customtkinter import CTkButton, CTkFrame
from components import entryInput

EntryInput = entryInput.EntryInput
operations = [
    {
        "symb": "÷",
        "value": "/",
    },
    {
        "symb": "x",
        "value": "*",
    },
    {
        "symb": "-",
        "value": "-",
    },
    {
        "symb": "+",
        "value": "+",
    },
]


class NumericPad:

    @staticmethod
    def handleClick(value):
        EntryInput.handleEntryValue(value)

    @staticmethod
    def init(root):
        col = 2
        row = 0

        frame = CTkFrame(root)
        frame.pack(fill="both", expand=True)
        frame.rowconfigure([0, 1, 2, 3], weight=1)
        frame.columnconfigure([0, 1, 2, 3], weight=1)

        for i in range(9, 0, -1):
            button = CTkButton(
                frame,
                text=i,
                command=lambda x=i: NumericPad.handleClick(x),
                height=70,
                fg_color="#C7C7C7",
                hover_color="#bbb",
                font=("Arial", 20),
                text_color="#000",
            )
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            col = col - 1 if col > 0 else 2
            row = row + 1 if col == 2 else row

        button = CTkButton(
            frame,
            text=".",
            height=70,
            command=lambda: NumericPad.handleClick("."),
            fg_color="#C7C7C7",
            text_color="#000",
            hover_color="#bbb",
            font=("Arial", 20),
        )
        button.grid(row=3, column=1, sticky="nsew", padx=5, pady=5, columnspan=2)

        button = CTkButton(
            frame,
            text="0",
            height=70,
            command=lambda: NumericPad.handleClick(0),
            fg_color="#C7C7C7",
            hover_color="#bbb",
            font=("Arial", 20),
            text_color="#000",
        )
        button.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

        row = 0
        for operation in operations:
            button = CTkButton(
                frame,
                text=operation["symb"],
                height=70,
                command=lambda x=operation["value"]: NumericPad.handleClick(x),
                fg_color="#C7C7C7",
                hover_color="#bbb",
                font=("Arial", 20),
                text_color="#000",
            )
            button.grid(
                row=row,
                column=3,
                sticky="nsew",
                padx=5,
                pady=5,
            )

            row = row + 1 if row < 3 else 0
