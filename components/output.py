from customtkinter import CTkScrollableFrame
from services.method import Method
from components.exceptions import Exceptions


class Output:
    outputArea = CTkScrollableFrame

    @staticmethod
    def print():
        # Destruir label de error si existe para no duplicar. Distintos tipos de excepciones para dar mensajes más específicos
        Exceptions.destroyLabel()
        try:
            frame, plotter = Method.calculateGx()
            frame.pack(
                padx=10,
                pady=10,
                fill="both",
            )
            if plotter is not None :
                plotter.show()
        except MemoryError:
            Exceptions.showError("Números demasiado grandes, posible divergencia")
        except OverflowError:
            Exceptions.showError("Números demasiado grandes, posible divergencia")
        except ZeroDivisionError:
            Exceptions.showError("División por cero")
        except ArithmeticError:
            Exceptions.showError("Operación no válida")
        except ValueError:
            Exceptions.showError("Error de Sintaxis")
        except Exception as e:
            Exceptions.showError(e)

    @staticmethod
    def init(root):
        Output.outputArea = CTkScrollableFrame(
            master=root,
            fg_color="white",
        )
        Output.outputArea.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10,
        )
        Output.outputArea.columnconfigure(0, weight=1)

        return Output.outputArea
