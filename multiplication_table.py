from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('800x1000')

window.focus_force()

variable = IntVar()

dropdown = Combobox(window, textvariable=variable)
dropdown.place(x=200, y=200)

dropdown['values'] = tuple(range(1,101))


radio_variable = IntVar(value=10)


for i in range(3):
    radio_button = Radiobutton(window, variable=radio_variable, text=f'{(i+1)*10}', value=(i+1)*10)
    radio_button.place(x=500, y=200 + i*30)
    
    
    
def multiply():
    list_frame = Frame(window)
    list_frame.place(x=0, y=300)
    scrollbar = Scrollbar(list_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    the_list = Listbox(list_frame, width=30, height=20, font=('Arial', 20), background='red', yscrollcommand=scrollbar.set)
    the_list.pack(side=LEFT, padx=10)


    scrollbar.config(command=the_list.yview)
    
    number = int(dropdown.get())
    the_range = radio_variable.get()
    for i in range(1, the_range+1):
        result = number * i
        string_result = f'{number} x {i} = {result}'
        the_list.insert(END, string_result)
        


done_button = Button(window, text='multiply', command=multiply)
done_button.place(x=400, y=450)

window.mainloop()