from tkinter import *
from tkinter import messagebox
import time

window = Tk()
window.title('Timer')
window.geometry('800x500')
window.focus_force()


def send_message():
    messagebox.showinfo(message = "Time's up!")

# def update_time():
#     current_time_left[2] -= 1
#     if current_time_left[2] < 0:
#         current_time_left[2] = 0
#         current_time_left[1]-= 1
#         if current_time_left[1] < 0:
#             current_time_left[1] = 0
#             current_time_left[0] -= 1
#             if current_time_left[0] < 0:
#                 current_time_left[1] = 0
#                 current_time_left[0] = 0
#                 send_message()
#                 return
    # for i in range (3):
    #     the_entries[i].config(text=str(current_time_left[i]))
#     window.after(1000, update_time)

entry_variables = [StringVar(value='0'), StringVar(value='0'), StringVar(value='0')]


hour_entry = Entry(window, width=5, text='0', textvariable=entry_variables[0])
hour_entry.place(x=100, y=200)
# the_entries.append(hour_entry)

minut_entry = Entry(window, width=5, text='0', textvariable=entry_variables[0])
minut_entry.place(x=400, y=200)
# the_entries.append(minut_entry)

second_entry = Entry(window, width=5, text='0', textvariable=entry_variables[0])
second_entry.place(x=700, y=200)
# the_entries.append(second_entry)

start_button = Button(window, text='Start')
start_button.place(x=400, y=400)

current_time_left = [0,0,0]




window.mainloop()