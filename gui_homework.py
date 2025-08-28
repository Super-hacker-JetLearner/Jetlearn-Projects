from tkinter import *
import tkinter


window = Tk()
window.title('Replit New Project')
window.geometry('450x300')
# window.config(background='blue')

top_button = Button(window, text='top')
top_button.pack(side='top')

right_button = Button(window, text='right')
right_button.pack(side='right')

left_button = Button(window, text='left', highlightbackground='blue', fg='red')
left_button.pack(side='left')

bottom_button = Button(window, text='bottom')
bottom_button.pack(side='bottom')

pick_template_label = Label(window, text='pick template')
pick_template_label.place(x=50, y=50)

name_project_label = Label(window, text='name project', background='red')
name_project_label.place(x=50, y=150)

pick_template_entry = Entry(window)
pick_template_entry.place(x=150, y=50)

name_project_entry = Entry(window)
name_project_entry.place(x=150, y=150)

create_replit_button = Button(window, text='Create Replit', background='blue')
create_replit_button.place(x=150, y=200)


window.mainloop()