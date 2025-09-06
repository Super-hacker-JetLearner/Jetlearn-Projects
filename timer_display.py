from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.title('Timer')
window.geometry('800x500')
window.focus_force()


def send_message():
    messagebox.showinfo(message = "Time's up!")

def update_time():
    entry_variables[0].set(int(entry_variables[0].get()) - 1)
    if int(entry_variables[0].get()) < 0:
        entry_variables[2].set(0)
        entry_variables[1].set(int(entry_variables[1].get()) - 1)
        if int(entry_variables[1].get()) < 0:
            entry_variables[1].set(0)
            entry_variables[2].set(int(entry_variables[2].get()) - 1)
            if int(entry_variables[0].get()) < 0:
                entry_variables[1].set(0)
                entry_variables[2].set(0)
                send_message()
                return

    window.after(1000, update_time)

entry_variables = [StringVar(value='0'), StringVar(value='0'), StringVar(value='0')]


hour_entry = Entry(window, width=5, text='0', textvariable=entry_variables[2])
hour_entry.place(x=100, y=200)
# the_entries.append(hour_entry)

minut_entry = Entry(window, width=5, text='0', textvariable=entry_variables[1])
minut_entry.place(x=400, y=200)
# the_entries.append(minut_entry)

second_entry = Entry(window, width=5, text='0', textvariable=entry_variables[0])
second_entry.place(x=700, y=200)
# the_entries.append(second_entry)

start_button = Button(window, text='Start', command=update_time)
start_button.place(x=400, y=400)





window.mainloop()