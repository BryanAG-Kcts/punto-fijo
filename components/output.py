from customtkinter import CTkScrollableFrame
from services.method import Method
from components.exceptions import Exceptions


class Output:
    outputArea = CTkScrollableFrame

    @staticmethod
    def print():
        Exceptions.destroyLabel()
        try:
            frame = Method.calculateGx()
            frame.pack(
                padx=10,
                pady=10,
                fill="both",
            )
        except MemoryError:
            Exceptions.showError("Números demasiado grandes, posible divergencia")
        except OverflowError:
            Exceptions.showError("Números demasiado grandes, posible divergencia")
        except ZeroDivisionError:
            Exceptions.showError("División por cero")
        except IndexError:
            Exceptions.showError("Campo(s) nulo")
        except KeyError:
            Exceptions.showError("Campo(s) nulo")
        except AttributeError:
            Exceptions.showError("Campo(s) nulo")
        except ArithmeticError:
            Exceptions.showError("Operación no válida o posible división por cero")
        except ValueError:
            Exceptions.showError("Campo(s) nulo")
        except NameError:
            Exceptions.showError(
                "Variable no definida o campo nulo. Recuerda, f(x) debe estar en función de x"
            )
        except TypeError:
            Exceptions.showError("Operación no válida")
        except SyntaxError:
            Exceptions.showError("Operación no válida")
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
