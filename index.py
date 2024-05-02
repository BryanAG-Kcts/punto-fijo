from customtkinter import CTk, CTkFrame, CTkTabview
import customtkinter

customtkinter.set_appearance_mode("light")

from components import (
    entryInput,
    numericPad,
    firstValueInput,
    output,
    errorInput,
    enterButton,
    exceptions,
    mathFunctionsBoard,
)

from services import method
from documentation import docs as doc
from documentation.constants import DocConstants

# Desestructurar clases, métodos y atributos
EntryInput = entryInput.EntryInput
NumericPad = numericPad.NumericPad
FirstValueInput = firstValueInput.FirstValueInput
ErrorInput = errorInput.ErrorInput
Output = output.Output
EnterButton = enterButton.EnterButton
Exceptions = exceptions.Exceptions
Method = method.Method
MathFunctionsBoard = mathFunctionsBoard.MathFunctionsBoard
Docs = doc.Docs

# app config
app = CTk()
app.geometry("1024x720")
app._set_appearance_mode("light")
app.title("Método de punto fijo 192096")
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)
# Global Frames
mainTab = CTkTabview(app)
mainTab.grid(row=0, column=0, sticky="nsew")
mainTab.columnconfigure(0, weight=1)

index = mainTab.add("Método de punto fijo")
docs = mainTab.add("Manual de uso")
index.columnconfigure(0, weight=1)
index.rowconfigure(0, weight=1)
docs.columnconfigure(0, weight=1)
docs.rowconfigure(1, weight=1)

inputFrame = CTkFrame(index)
inputFrame.grid(row=1, column=0, sticky="nsew", pady=10)
inputFrame.columnconfigure(0, weight=5)
inputFrame.columnconfigure([1, 2, 3], weight=1)
inputFrame.rowconfigure(0, weight=1)

tabView = CTkTabview(index)
tabView.grid(row=2, column=0, sticky="nsew")
opBasicas = tabView.add("Números y operaciones básicas")
mathFunctions = tabView.add("Funciones matemáticas")

# inits
DocConstants.init()

EntryInput.init(inputFrame)
FirstValueInput.init(inputFrame)
ErrorInput.init(inputFrame)
EnterButton.init(inputFrame)

Docs.init(docs)
outputArea = Output.init(index)
Method.setOutputArea(outputArea)
Exceptions.init(index)
NumericPad.init(opBasicas)
MathFunctionsBoard.init(mathFunctions)

app.mainloop()
