

import tkinter as tk

window = tk.Tk()

window.title("Last Mouse Lost")
window.geometry('1024x768')
lbl = tk.Label(window, text="Welcome to Last Mouse Lost", font=("Arial Bold", 15))
lbl.pack()
window.ROWS = 6
window.COLS = 6
window.WIDTH = 800
window.HEIGHT = 600
window.col_width = window.WIDTH / window.COLS
window.row_height = window.HEIGHT / window.ROWS
window.c = tk.Canvas(window, width=window.WIDTH, height=window.HEIGHT, borderwidth=5, background='blue')
x=50
y=50
z=50
w=50
for ROWS in range(1):
    for COLS in range(2, 5):
        oval=window.c.create_oval(x, y, z, w, fill="red")
        x=+1
        y=+1
        z=+1
        w=+1

window.c.pack()
'''for ROWS in range(1):
    for COLS in range(2, 5):
            window.c.create_oval( fill="gray", outline="gray").grid(row=ROWS, column=COLS)

for ROWS in range(2, 3):
    for COLS in range(1, 6):
            window.c.create_oval( fill="gray", outline="gray").grid(row=ROWS, column=COLS)

for ROWS in range(3, 4):
    for COLS in range(6):
            window.c.create_oval( fill="gray", outline="gray").grid(row=ROWS, column=COLS)

for ROWS in range(4, 5):
    for COLS in range(6):
            window.c.create_oval( fill="gray", outline="gray").grid(row=ROWS, column=COLS)

for ROWS in range(5, 6):
    for COLS in range(1, 6):
            window.c.create_oval( fill="gray", outline="gray").grid(row=ROWS, column=COLS)

for ROWS in range(6, 7):
    for COLS in range(2, 5):
            window.c.create_oval( fill="gray", outline="gray").grid(row=ROWS, column=COLS)'''

"""for i in range(6):
    for j in range(6):
        if (i + j) % 2 == 1:
            window.c.create_oval(i * window.row_height, j * window.col_width,
                                    (i + 1) * window.row_height, (j + 1) * window.col_width, fill="gray", outline="gray")
#window.c.pack()
"""

"""
def donothing():
    mainwindow = tk.Toplevel(window)
    mainwindow.geometry('1024x768')
    button = tk.Button(mainwindow, text="Do nothing button")
    button.pack()


def humanvhuman():
    mainwindow = tk.Toplevel(window)
    # lbl1 = tk.Label(mainwindow, text="Welcome to Last Mouse Lost",font=("Arial Bold", 20)).grid(row=10)
    mainwindow.geometry('1024x768')
    for r in range(1):
        for c in range(2, 5):
            tk.Button(mainwindow, text='', padx='50', pady='20', bg="red", borderwidth=1).grid(row=r, column=c)

    for r in range(2, 3):
        for c in range(1, 6):
            tk.Button(mainwindow, text='', padx='50', pady='20', bg="yellow", borderwidth=1).grid(row=r, column=c)

    for r in range(3, 4):
        for c in range(6):
            tk.Button(mainwindow, text='', padx='50', pady='20', bg="green", borderwidth=1).grid(row=r, column=c)

    for r in range(4, 5):
        for c in range(6):
            tk.Button(mainwindow, text='', padx='50', pady='20', bg="green", borderwidth=1).grid(row=r, column=c)

    for r in range(5, 6):
        for c in range(1, 6):
            tk.Button(mainwindow, text='', padx='50', pady='20', bg="yellow", borderwidth=1).grid(row=r, column=c)

    for r in range(6, 7):
        for c in range(2, 5):
            tk.Button(mainwindow, text='', padx='50', pady='20', bg="red", borderwidth=1).grid(row=r, column=c)


def humanvai():
    mainwindow = tk.Toplevel(window)
    mainwindow = tk.Canvas(mainwindow, bg="blue", height=768, width=1024)
    mainwindow.pack()


def helpwindow():
    mainwindow = tk.Toplevel(window)
    mainwindow = tk.Canvas(mainwindow, bg="blue", height=768, width=1024)
    mainwindow.pack()


def aboutwindow():
    mainwindow = tk.Toplevel(window)
    mainwindow = tk.Canvas(mainwindow, bg="blue", height=768, width=1024)
    mainwindow.pack()


menu = tk.Menu(window)

gamemenu = tk.Menu(menu)
gamemenu.add_command(label='New Game', command=humanvai)
gamemenu.add_command(label='Load Game', command=donothing)
gamemenu.add_command(label='Exit', command=window.quit)
menu.add_cascade(label='Game', menu=gamemenu)

setttingsmenu = tk.Menu(menu)
setttingsmenu.add_command(label='Human vs Human', command=humanvhuman)
setttingsmenu.add_command(label='Human vs AI', command=humanvai)
menu.add_cascade(label='Settings', menu=setttingsmenu)

helpmenu = tk.Menu(menu)
helpmenu.add_command(label='How to play', command=helpwindow)
helpmenu.add_command(label='About', command=aboutwindow)
menu.add_cascade(label='Help', menu=helpmenu)
window.config(menu=menu)
"""
window.mainloop()