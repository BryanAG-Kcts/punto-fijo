from customtkinter import CTkButton
from components import output

Output = output.Output


class EnterButton:
    button = CTkButton

    @staticmethod
    def handleClick():
        Output.print()

    @staticmethod
    def init(root):
        EnterButton.button = CTkButton(
            root,
            text="Enter",
            height=70,
            command=lambda: EnterButton.handleClick(),
            font=("Arial", 20),
        )
        EnterButton.button.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
