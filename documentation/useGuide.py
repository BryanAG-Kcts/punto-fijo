from customtkinter import CTkLabel, CTkFrame
from documentation.constants import DocConstants


class UseGuide:

    @staticmethod
    def init(root):
        CTkLabel(
            root,
            font=DocConstants.h1Size,
            text="GUÍA DE USO",
        ).pack()

        flex = CTkFrame(root, fg_color="#e0e0e0")
        flex.pack()

        CTkLabel(
            flex,
            font=DocConstants.pSize,
            text="Input de entrada: ",
            text_color="#4fa7eb",
        ).grid(column=0, row=0)

        CTkLabel(
            flex,
            font=DocConstants.pSize,
            text="Input de entrada",
        ).grid(column=1, row=0)
