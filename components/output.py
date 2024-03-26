from customtkinter import CTkScrollableFrame
from services import method

Method = method.Method


class Output:
    row = 0
    outputArea = CTkScrollableFrame

    @staticmethod
    def print():
        frame = Method.generateTable()
        frame.master = Output.outputArea
        frame.grid(row=Output.row, column=0, sticky="nsew", padx=10, pady=10)
        Output.row += 1

    @staticmethod
    def init(root):
        Output.outputArea = CTkScrollableFrame(master=root, fg_color="white")
        Output.outputArea.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
