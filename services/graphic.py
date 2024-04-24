from sympy.plotting import plot
from sympy import Symbol, plot_implicit, Eq
from customtkinter import CTkImage, CTkLabel
from PIL import Image


class Graphic:

    graphicCounter = 0

    @staticmethod
    def generateGraphic(root, gx, rows, x0, xf):
        x = Symbol("x")
        functionRange = (x, x0 - 1, xf + 1)
        plotter = plot(gx, functionRange, show=False, line_color="red", ylabel=gx)
        plotter.append(plot(x, functionRange, show=False, line_color="blue")[0])
        plotter.append(plot_implicit(Eq(x, xf), show=False, line_color="green")[0])
        plotter.save(f"images/graph_{Graphic.graphicCounter}.png")
        img = Image.open(f"images/graph_{Graphic.graphicCounter}.png")

        image = CTkImage(img, size=(400, 400))
        canvas = CTkLabel(root, image=image, text="")
        canvas.grid(row=rows, column=0, columnspan=4, sticky="nsew", pady=20)
        Graphic.graphicCounter += 1
