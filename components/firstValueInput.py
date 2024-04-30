from customtkinter import CTkEntry


class FirstValueInput:

    entry = CTkEntry

    @staticmethod
    def init(root):
        FirstValueInput.entry = CTkEntry(
            root,
            height=70,
            placeholder_text="Ingresar valor inicial X0",
            font=("Arial", 20),
            justify="center",
        )
        FirstValueInput.entry.grid(row=0, column=1, sticky="nsew", padx=5)

    def getValue():
        # Si el valor ingresado es vacío, se asigna 0
        return FirstValueInput.entry.get() or 0
