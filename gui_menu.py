import tkinter
from tkinter import *


window = Tk()
window.geometry('450x300')
window.title('gui menu')

menu = Menu(window)
file = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=file)
file.add_command(label='save', command=None)

# window.config(menu=menu)
window.configure(menu=menu)

window.mainloop()