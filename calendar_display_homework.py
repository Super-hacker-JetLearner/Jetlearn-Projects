import calendar
from tkinter import *
import tkinter

window = Tk()
window.geometry('500x250')
window.config(background='light blue')
window.title('calendar home page')



    



def make_home():
    global calendar_label, enter_year_label, enter_year_entry, show_calendar_button, exit_button
    window.geometry('500x250')
    calendar_label = Label(window, text='CALENDAR', background='grey', font=("Arial", 25))
    calendar_label.pack(side='top')
    enter_year_label = Label(window, text='Enter Year', background='green')
    enter_year_label.place(x=225, y=50)
    enter_year_entry = Entry(window)
    enter_year_entry.place(x=175, y=100)
    show_calendar_button = Button(window, text='Show Calendar', command=go_to_calendar)
    show_calendar_button.place(x=200, y=150)
    exit_button = Button(window, text='Exit', command=exit_all)
    exit_button.place(x=200, y=200)
    

def show_calendar(year):
    global calendar_label, the_calendar, go_back_button
    calendar_window = Tk()
    calendar_window.geometry('550x700')
    calendar_window.title(f'year: {year}')
    the_calendar = calendar.calendar(year)
    calendar_label = Label(calendar_window, text=the_calendar, font=("Arial", 15))
    calendar_label.place(x=0, y=0)
    go_back_button = Button(calendar_window, command=calendar_window.destroy, text='go back')
    go_back_button.place(x=250, y=650)
    

    
def go_to_calendar():
    year = enter_year_entry.get()
    show_calendar(int(year))
    
    
def exit_all():
    print('bye!')
    exit()
    
make_home()

window.mainloop()