from tkinter import *
from tkinter.ttk import *

window = Tk()
window.config(background='light grey')
window.geometry('800x500')
window.title('Pizza Hut')
window.focus_force()

welcome_label = Label(window, text='Welcome to Pizza Hut')
welcome_label.pack()

pizza_label = Label(window, text='Select your Fav Pizza: ')
pizza_label.place(x=0, y=150)

pizza_variable = StringVar()

pizza_choice = Combobox(window, textvariable=pizza_variable, state='readonly')
pizza_choice.place(x=200, y=150)
pizza_choice['values'] = ['Veg Extravaganza', 'Pepperoni', 'Margherita', 'Pineapple']
pizza_choice.current(0)

quantity_label = Label(window, text='Enter Quantity: ')
quantity_label.place(x=0, y=200)

quantity_variable = IntVar()

quantity_choice = Combobox(window, textvariable=quantity_variable)
quantity_choice.place(x=200, y=200)
quantity_choice['values'] = list(range(1, 101))
quantity_choice.current(0)

size_variable = StringVar(value='Small')
radio_frame = Frame(window)
radio_frame.pack(side=RIGHT)

style = Style(window)
style.configure("TRadiobutton", font = ("arial", 25, "bold"))


small_radio = Radiobutton(radio_frame, variable=size_variable, text='S', value='Small')
small_radio.pack()
medium_radio = Radiobutton(radio_frame, variable=size_variable, text='M', value='Medium')
medium_radio.pack()
large_radio = Radiobutton(radio_frame, variable=size_variable, text='L', value='Large')
large_radio.pack()

ordered_variable = StringVar()

ordered_label = Label(window, textvariable=ordered_variable)
ordered_label.place(x=400, y=400)
def display_order():
    result = f'You ordered {quantity_variable.get()} {pizza_variable.get()} {size_variable.get()} Size Pizza(s)'
    ordered_variable.set(result)

order_button = Button(window, text='Order', command=display_order)
order_button.place(x=400, y=300)

window.mainloop()
