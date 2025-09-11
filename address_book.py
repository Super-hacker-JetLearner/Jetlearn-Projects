from tkinter import *

window = Tk()
window.geometry('800x800')

window.focus_force()

right_side_frame = Frame(window)
right_side_frame.pack(side=RIGHT)

entries_frame = Frame(right_side_frame)
entries_frame.pack(side=RIGHT, padx=20)

name_entry = Entry(entries_frame)
name_entry.pack(pady=10)
address_entry = Entry(entries_frame)
address_entry.pack(side=BOTTOM, pady=10)
phone_entry = Entry(entries_frame)
phone_entry.pack(side=BOTTOM, pady=10)
email_entry = Entry(entries_frame)
email_entry.pack(side=BOTTOM, pady=10)

labels_frame = Frame(right_side_frame)
labels_frame.pack(side=LEFT, padx=20)

name_label = Label(labels_frame, text='Name: ')
name_label.pack(side=BOTTOM, pady=10)
address_label = Label(labels_frame, text='Address: ')
address_label.pack(side=BOTTOM, pady=10)
phone_label = Label(labels_frame, text='Phone: ')
phone_label.pack(side=BOTTOM, pady=10)
email_label = Label(labels_frame, text='Email: ')
email_label.pack(side=BOTTOM, pady=10)



window.mainloop()