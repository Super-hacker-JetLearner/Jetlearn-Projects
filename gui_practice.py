from tkinter import *

top = Tk()
top.title('Login Page')
top.geometry('450x300')
top.config(background='blue')

username_label = Label(top, text='Username', borderwidth=5)
username_label.place(x=10,y=10)

username_input = Entry(top)
username_input.place(x=100,y=10)

done_button = Button(top, text='done', foreground='blue')
done_button.place(x=100, y=100)

top.mainloop()