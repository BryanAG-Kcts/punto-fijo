from sympy.plotting import plot
from sympy import Symbol, plot_implicit, Eq
from customtkinter import CTkImage, CTkLabel
from PIL import Image


class Graphic:

    graphicCounter = 1
    isDocs = True

    @staticmethod
    def generateGraphic(root, gx, rows, xf):
        if Graphic.isDocs:
            Graphic.isDocs = False
            img = Image.open("images/graph_0.png")
            image = CTkImage(img, size=(400, 400))
            canvas = CTkLabel(root, image=image, text="")
            canvas.grid(row=rows, column=0, columnspan=4, sticky="nsew", pady=20)
            return None

        x = Symbol("x")
        plotter = plot(
            gx,
            show=False,
            line_color="red",
            ylabel=gx,
            legend=True,
        )
        plotter.append(
            plot(
                x,
                show=False,
                line_color="blue",
                legend=True,
            )[0]
        )
        plotter.append(
            plot(
                xf,
                show=False,
                line_color="#263238",
                lengend=True,
            )[0]
        )
        plotter.append(
            plot_implicit(
                Eq(x, xf),
                show=False,
                line_color="green",
                legend=True,
            )[0]
        )
        plotter.save(f"images/graph_{Graphic.graphicCounter}.png")
        img = Image.open(f"images/graph_{Graphic.graphicCounter}.png")

        image = CTkImage(img, size=(400, 400))
        canvas = CTkLabel(root, image=image, text="")
        canvas.grid(row=rows, column=0, columnspan=4, sticky="nsew", pady=20)
        Graphic.graphicCounter += 1

        return plotter
