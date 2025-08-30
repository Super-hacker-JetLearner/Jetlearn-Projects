from tkinter import *

window = Tk()
window.geometry('500x500')

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)


the_list = Listbox(window, width=15, height=15, font=('Arial', 20), background='blue', yscrollcommand=scrollbar.set)
the_list.pack(side=TOP)

scrollbar.config(command=the_list.yview)

for i in range (100):
    the_list.insert(END, 'hi'+ str(i))

window.mainloop()