from customtkinter import CTk, CTkFrame
from components import (
    entryInput,
    numericPad,
    firstValueInput,
    output,
    errorInput,
    enterButton,
)

# Desestructurar métodos y atributos
EntryInput = entryInput.EntryInput
NumericPad = numericPad.NumericPad
FirstValueInput = firstValueInput.FirstValueInput
ErrorInput = errorInput.ErrorInput
Output = output.Output
EnterButton = enterButton.EnterButton

# app config
app = CTk()
app.geometry("1024x720")
app._set_appearance_mode("light")
app.title("Método de punto fijo 192096")
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

# Global Frames
inputFrame = CTkFrame(app)
inputFrame.grid(row=1, column=0, sticky="nsew")
inputFrame.columnconfigure(0, weight=5)
inputFrame.columnconfigure([1, 2, 3], weight=1)
inputFrame.rowconfigure(0, weight=1)

# inits

EntryInput.init(inputFrame)
FirstValueInput.init(inputFrame)
ErrorInput.init(inputFrame)
EnterButton.init(inputFrame)

Output.init(app)
NumericPad.init(app)
app.mainloop()
