from customtkinter import CTkButton
from components import output, exceptions

Output = output.Output
Exceptions = exceptions.Exceptions


class EnterButton:
    button = CTkButton

    @staticmethod
    def handleClick():
        Exceptions.destroyLabel()
        try:
            Output.print()
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
        EnterButton.button = CTkButton(
            root,
            text="Enter",
            height=70,
            command=lambda: EnterButton.handleClick(),
            font=("Arial", 20),
        )
        EnterButton.button.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)
