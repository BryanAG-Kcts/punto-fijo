from customtkinter import CTkLabel


class Exceptions:

    label = None
    root = None

    @staticmethod
    def init(root):
        Exceptions.root = root

    @staticmethod
    def showError(exception):

        Exceptions.destroyLabel()
        Exceptions.label = CTkLabel(
            Exceptions.root,
            text=exception,
            fg_color="#ffdfdf",
        )
        Exceptions.label.grid(
            row=3,
            column=0,
            sticky="nsew",
        )

    @staticmethod
    def destroyLabel():
        # Destruir label para que no se dupliquen
        if Exceptions.label is not None:
            Exceptions.label.destroy()
