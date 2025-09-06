from tkinter import *
from tkinter import messagebox
from random import *

window = Tk()
window.geometry('500x300')
window.title('Guess the Number Game!')

window.focus_force()

name = 'Unknown User'
number = randint(0,20)

def set_name():
    global name
    name = name_entry.get()
    name_entry.delete(0, END)

title_label = Label(window, text='Welcome to our game!')
title_label.pack()
name_label = Label(window, text="What's your name?")
name_label.place(x=0, y=40)
name_entry = Entry(window)
name_entry.place(x=0, y=80)
ok_button = Button(window, text='OK', command=set_name)
ok_button.place(x=150, y=80)

def show_message_box():
    guess = int(guess_entry.get())
    if guess < number:
        messagebox.showinfo(message=f'Hello {name}! That is too small!')
        window.focus()
    elif guess > number:
        messagebox.showinfo(message=f'Hello {name}! That is too big!')
        window.focus()
    elif guess == number:
        messagebox.showinfo(message=f'Hello {name}! You won!')
        window.focus()
        

range_label = Label(window, text='Choose a number between 0 and 20!')
range_label.place(x=0, y=120)
guess_label = Label(window, text='Take a guess:')
guess_label.place(x=0, y=160)
guess_entry = Entry(window, width=10)
guess_entry.place(x=100, y=160)
guess_button = Button(window, text='Guess', command=show_message_box)
guess_button.place(x=200, y=160)

window.mainloop()