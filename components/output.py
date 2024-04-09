from customtkinter import CTkScrollableFrame
from services import method

Method = method.Method


class Output:
    outputArea = CTkScrollableFrame

    @staticmethod
    def print():
        frame = Method.generateTable()
        frame.pack(
            padx=10,
            pady=10,
            fill="both",
        )

    @staticmethod
    def init(root):
        Output.outputArea = CTkScrollableFrame(
            master=root,
            fg_color="white",
        )
        Output.outputArea.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10,
        )
        Output.outputArea.columnconfigure(0, weight=1)

        return Output.outputArea
