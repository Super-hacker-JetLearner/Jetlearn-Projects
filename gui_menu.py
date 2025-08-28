from tkinter import *
from tkinter.ttk import *


window = Tk()
window.geometry('450x300')
window.title('gui menu')

menu = Menu(window)

file = Menu(menu)
menu.add_cascade(label='File', menu=file)
file.add_command(label='save', command=None)
file.add_command(label='open file', command=None)
file.add_separator()
file.add_command(label='exit', command=None)

edit = Menu(menu)
menu.add_cascade(label='edit', menu=edit)
edit.add_command(label='change text', command=None)
edit.add_command(label='change style', command=None)
edit.add_separator()
edit.add_command(label='exit edit mode', command=None)


window.config(menu=menu)
# window.configure(menu=menu)


window.mainloop()