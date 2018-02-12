import tkinter
import math


def parabola(page, size):
    for x in range(size):
        y = x*x/size
        plot(page, x, y)
        plot(page, -x, y)


def circle(page, radius=25, g=0, h=0, line_color='Black', width=2, fill=None):
    page.create_oval(g+radius, h+radius, g-radius, h-radius, outline=line_color, width=width, fill=fill)
    # for x in range(g*100, (g+ radius)*100):
    #     x /= 100
    #     print(x)
    #     y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, y_origin, 0, -y_origin, fill='black')
    print(locals())


def plot(page, x, y):
    page.create_line(x, y, x+1, y+1, fill='red', smooth=True, splinesteps=12)


mainWindow = tkinter.Tk()

mainWindow.title('Parabola')
mainWindow.geometry('800x800')

canvas = tkinter.Canvas(mainWindow, width=800, height=800)
canvas.grid(row=0, column=0)

draw_axes(canvas)

# parabola(canvas, 100)
# parabola(canvas, 200)
circle(canvas, 72, 72, -72, 'Red', 2, 'Blue')


mainWindow.mainloop()
