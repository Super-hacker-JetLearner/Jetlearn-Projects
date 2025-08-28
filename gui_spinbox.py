from tkinter import *

window = Tk()
window.geometry('450x300')
window.title('spinbox')

spinbox = Spinbox(window, from_=0, to=10)
spinbox.pack(side='left')

window.mainloop()