from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.config(background='light grey')
window.geometry('800x500')

window.focus_force()

top_frame = Frame(window)
top_frame.pack(side=TOP)

def save_file():
    new_file = asksaveasfile(defaultextension='.txt')
    if new_file is not None:
        for i in the_list.get(0, END):
            print(i, file=new_file)
        the_list.delete(0, END)

def open_file():
    the_file = askopenfile(title='Open File', defaultextension='.txt')
    if the_file is not None:
        the_list.delete(0, END)
        data = the_file.readlines()
        for i in data:
            the_list.insert(END, i)

open_button = Button(top_frame, text='OPEN', font=('Arial', 25), width=8, command=open_file)
open_button.pack(side=RIGHT, padx=10)

def delete_thing():
    the_index = the_list.curselection()
    if the_index:
        the_list.delete(the_index)

delete_button = Button(top_frame, text='DELETE', font=('Arial', 25), width=8, command=delete_thing)
delete_button.pack(side=RIGHT, padx=10)

save_button = Button(top_frame, text='SAVE', font=('Arial', 25), width=8, command=save_file)
save_button.pack(side=RIGHT, padx=10)

entry = Entry(window)
entry.pack(side=RIGHT)

def add_thing():
    the_list.insert(END, entry.get())
    entry.delete(0, END)


add_button = Button(window, text='ADD', font=('Arial', 25), command=add_thing)
add_button.place(x=670, y=350)



scrollbar = Scrollbar(window)
scrollbar.place(x=550, y=50, height=430)

the_list = Listbox(window, width=45, height=18, font=('Arial', 20), background='red', yscrollcommand=scrollbar.set)
the_list.place(x=0, y=50)

scrollbar.config(command=the_list.yview)

for i in range (100):
    the_list.insert(END, f'LIST {i+1}')


window.mainloop()