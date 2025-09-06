from tkinter import *
import tkinter
from time import strftime, sleep
from random import choice

window = Tk()
# window.geometry('500x300')
window.focus_force()

current_time = StringVar()

colors = ['blue', 'red', 'green', 'yellow', 'light blue', 'pink', 'purple', 'brown', 'grey', 'black', 'white']
foreground = 'red'
background = 'blue'

def update_time():
    global background, foreground
    the_time = strftime('%H:%M:%S %p')
    current_time.set(the_time)
    time_label.after(1000, update_time)
    foreground = choice(colors)
    background = choice(colors)
    while foreground == background:
        foreground = choice(colors)
        background = choice(colors)
    time_label.config(background=background, foreground=foreground)
    

time_label = Label(window, textvariable=current_time, font=('Arial', 50, 'bold'), foreground='red', background='blue')
time_label.pack()
time_label.after(1000, update_time)

window.mainloop()