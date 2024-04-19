from sympy.plotting import plot
from sympy import Symbol
from customtkinter import CTkImage, CTkLabel
from PIL import Image


class Graphic:

    graphicCounter = 0

    @staticmethod
    def generateGraphic(root, fx, gx, rows, x0, xf):
        x = Symbol("x")
        functionRange = (x, x0, xf)
        plotter = plot(gx, functionRange, show=False, line_color="red", ylabel=fx)
        plotter.append(plot(fx, functionRange, show=False, line_color="blue")[0])
        plotter.save(f"images/graph_{Graphic.graphicCounter}.png")
        img = Image.open(f"images/graph_{Graphic.graphicCounter}.png")

        image = CTkImage(img, size=(400, 400))
        canvas = CTkLabel(root, image=image, text="")
        canvas.grid(row=rows, column=0, columnspan=4, sticky="nsew", pady=20)
        Graphic.graphicCounter += 1
