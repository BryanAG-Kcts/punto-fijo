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
        )
        FirstValueInput.entry.grid(row=0, column=1, sticky="nsew", padx=5)

    def getValue():
        return FirstValueInput.entry.get()
