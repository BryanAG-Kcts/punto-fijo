from customtkinter import CTkEntry
from services import operations

Operations = operations.Operations


class ErrorInput:
    entry = CTkEntry

    @staticmethod
    def init(root):
        ErrorInput.entry = CTkEntry(
            root,
            height=70,
            placeholder_text="Ingresar error",
            font=("Arial", 20),
            justify="center",
        )
        ErrorInput.entry.grid(row=0, column=2, sticky="nsew", padx=5)

    def getPercentValue():
        return Operations.parsePercent(float(ErrorInput.entry.get() or 0.01))
