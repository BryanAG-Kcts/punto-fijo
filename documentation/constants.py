from customtkinter import CTkFont


class DocConstants:
    h1Size = CTkFont
    h2Size = CTkFont
    h3Size = CTkFont
    pSize = CTkFont

    @staticmethod
    def init():

        DocConstants.h2Size = CTkFont(size=20, weight="bold")
        DocConstants.h1Size = CTkFont(size=35, weight="bold")
        DocConstants.h3Size = CTkFont(size=22, weight="bold")
        DocConstants.pSize = CTkFont(size=18)
