import tkinter


def parabola(page, size):
    for x in range(-size, size):
        y = x*x/size
        plot(page, x, y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, y_origin, 0, -y_origin, fill='black')
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x+1, -y+1, fill='red', smooth=True, splinesteps=12)


mainWindow = tkinter.Tk()

mainWindow.title('Parabola')
mainWindow.geometry('800x800')

canvas = tkinter.Canvas(mainWindow, width=800, height=800)
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

mainWindow.mainloop()
