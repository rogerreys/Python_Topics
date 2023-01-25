import numpy as np
import random

from bokeh.plotting import figure, output_file, show

def vectorizing(value):
    output_file('Grafico simple.html')
    # generate some data (1-10 for x, random values for y)
    x = list(range(0, value))
    y = random.sample(range(0, 100), value)

    # generate list of rgb hex colors in relation to y
    colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]

    # create new plot
    p = figure(
        title="Vectorized colors example",
        sizing_mode="stretch_width",
        max_width=500,
        height=250,
    )

    # add circle and line renderers
    line = p.line(x, y, line_color="red", line_width=1)
    circle = p.circle(x, y, fill_color=colors, line_color="blue", size=8)

    # show the results
    show(p)
    
def vectorizingSizes(len_value):
    # generate some data
    N=len_value
    x = np.random.random(size=N) * 100
    y = np.random.random(size=N) * 100
    
    # generate radii and colors based on data
    radii = y / 100 * 2

    # create a new plot with a specific size
    p = figure(
        title="Vectorized radii",
        # sizing_mode="stretch_width",
        max_width=500,
        height = 250
    )

    # add circle renderer
    p.circle(
        x,
        y,
        radius=radii
    )

    # Show the results
    show(p)

if __name__=='__main__':
    len_value = int(input('Cuantos valores desea ingresar: '))
    # vectorizing(len_value)
    vectorizingSizes(len_value)