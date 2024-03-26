from customtkinter import CTkLabel


class Exceptions:

    label = None
    root = None

    @staticmethod
    def init(root):
        Exceptions.root = root

    @staticmethod
    def showError(exception):
        if Exceptions.label is not None:
            Exceptions.label.destroy()

        Exceptions.label = CTkLabel(Exceptions.root, text=exception)
        Exceptions.label.grid(row=3, column=0)
