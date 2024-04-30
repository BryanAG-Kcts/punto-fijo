from sympy.plotting import plot
from sympy import Symbol, plot_implicit, Eq
from customtkinter import CTkImage, CTkLabel
from PIL import Image


class Graphic:

<<<<<<< HEAD
    graphicCounter = 1
=======
    graphicCounter = 0
    isDocs = True
>>>>>>> a64f7fd41e13693d98e04d6228003e92d29bfdb0

    @staticmethod
    def generateGraphic(root, gx, rows, x0, xf):
        if Graphic.isDocs :
            Graphic.isDocs = False
            img = Image.open("images/graph_0.png")
            image = CTkImage(img, size=(400, 400))
            canvas = CTkLabel(root, image=image, text="")
            canvas.grid(row=rows, column=0, columnspan=4, sticky="nsew", pady=20)
            Graphic.graphicCounter += 1
            return None
        
        x = Symbol("x")
        minRange = x0 - 1
        maxRange = xf + 1
        functionRange = (x, minRange, maxRange)
        plotter = plot(gx, functionRange, show=False, line_color="red", ylabel=gx)
        plotter.append(plot(x, functionRange, show=False, line_color="blue")[0])
        plotter.append(plot_implicit(Eq(x, xf), show=False, line_color="green")[0])
        plotter.save(f"images/graph_{Graphic.graphicCounter}.png")
        img = Image.open(f"images/graph_{Graphic.graphicCounter}.png")

        image = CTkImage(img, size=(400, 400))
        canvas = CTkLabel(root, image=image, text="")
        canvas.grid(row=rows, column=0, columnspan=4, sticky="nsew", pady=20)
        Graphic.graphicCounter += 1
                
        return plotter
