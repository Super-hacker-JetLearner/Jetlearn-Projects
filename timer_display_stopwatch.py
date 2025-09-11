from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.title('Timer')
window.geometry('800x500')
window.focus_force()

time_left = 0
timer_on = False


def send_message():
    messagebox.showinfo(message = "Time's up!")
    
def start_time():
    global time_left, timer_on
    timer_on = True
    time_left = int(hour_entry.get())*3600 + int(minut_entry.get())*60 + int(second_entry.get())
    update_time()

def update_time():
    global time_left
    if time_left == 0:
        send_message()
        return
    if not timer_on:
        return
    else:
        time_left -= 1
        hours, time_remainder = divmod(time_left, 3600)
        minutes, time_remainder = divmod(time_remainder, 60)
        seconds = round(time_remainder)
        
        hour_variable.set(str(hours))
        minut_variable.set(str(minutes))
        second_variable.set(str(seconds))
    
    
    window.after(1000, update_time)


hour_variable = StringVar(value='0')
hour_entry = Entry(window, width=5, textvariable=hour_variable)
hour_entry.place(x=100, y=200)
# the_entries.append(hour_entry)

minut_variable = StringVar(value='0')
minut_entry = Entry(window, width=5, textvariable=minut_variable)
minut_entry.place(x=400, y=200)
# the_entries.append(minut_entry)

second_variable = StringVar(value='0')
second_entry = Entry(window, width=5, textvariable=second_variable)
second_entry.place(x=700, y=200)
# the_entries.append(second_entry)

start_button = Button(window, text='Start', command=start_time)
start_button.place(x=400, y=400)
def cancel():
    global timer_on
    timer_on = False

stop_button = Button(window, text='Stop', command=cancel)
stop_button.place(x=500, y=400)



window.mainloop()