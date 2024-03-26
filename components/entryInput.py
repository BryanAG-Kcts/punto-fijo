from customtkinter import CTkEntry


class EntryInput:
    entry = CTkEntry

    @staticmethod
    def init(root):
        EntryInput.entry = CTkEntry(
            root,
            height=70,
            placeholder_text="Ingresar f(x)",
            font=("Arial", 20),
        )
        EntryInput.entry.grid(row=0, column=0, sticky="nsew", padx=5)

    @staticmethod
    def handleEntryValue(value):
        EntryInput.entry.insert("end", value)

    @staticmethod
    def getValue():
        return EntryInput.entry.get()
