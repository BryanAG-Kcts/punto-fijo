from customtkinter import CTk, CTkFrame, CTkTabview
from components import (
    entryInput,
    numericPad,
    firstValueInput,
    output,
    errorInput,
    enterButton,
    exceptions,
)

from services import method

# Desestructurar métodos y atributos
EntryInput = entryInput.EntryInput
NumericPad = numericPad.NumericPad
FirstValueInput = firstValueInput.FirstValueInput
ErrorInput = errorInput.ErrorInput
Output = output.Output
EnterButton = enterButton.EnterButton
Exceptions = exceptions.Exceptions
Method = method.Method

# app config
app = CTk()
app.geometry("1024x720")
app._set_appearance_mode("light")
app.title("Método de punto fijo 192096")
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

# Global Frames
inputFrame = CTkFrame(app, fg_color="#fff")
inputFrame.grid(row=1, column=0, sticky="nsew", pady=10)
inputFrame.columnconfigure(0, weight=5)
inputFrame.columnconfigure([1, 2, 3], weight=1)
inputFrame.rowconfigure(0, weight=1)

tabView = CTkTabview(app, fg_color="#fff")
tabView.grid(row=2, column=0, sticky="nsew")
opBasicas = tabView.add("Numeros y operaciones básicas")

# inits
EntryInput.init(inputFrame)
FirstValueInput.init(inputFrame)
ErrorInput.init(inputFrame)
EnterButton.init(inputFrame)

outputArea = Output.init(app)
Method.setOutputArea(outputArea)
Exceptions.init(app)
NumericPad.init(opBasicas)
app.mainloop()
