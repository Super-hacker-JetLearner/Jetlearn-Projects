from tkinter import *


window = Tk()
window.geometry('500x500')

frame = Frame(window)
frame.pack(side=TOP)

bottom_frame = Frame(window)
bottom_frame.pack(side=RIGHT)


button1 = Button(frame, text='dark choco', font=('Arial', 20))
button1.pack(side=LEFT)

button2 = Button(frame, text='milk choco', font=('Arial', 20))
button2.pack(side=LEFT)

button3 = Button(frame, text='white choco', font=('Arial', 20))
button3.pack(side=LEFT)


button4 = Button(bottom_frame, text='vanilla icecream', font=('Arial', 20))
button4.pack(side=BOTTOM)

button5 = Button(bottom_frame, text='choco icecream', font=('Arial', 20))
button5.pack(side=BOTTOM)

button6 = Button(bottom_frame, text='strawberry icecream', font=('Arial', 20))
button6.pack(side=BOTTOM)

window.mainloop()