from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

window = Tk()
window.geometry('600x520')
window.title('Address Book')

window.focus_force()

address_dictionary = {}

padding_y = 20

right_side_frame = Frame(window)
right_side_frame.pack(side=RIGHT, padx=20)

entries_frame = Frame(right_side_frame)
entries_frame.pack(side=RIGHT, padx=(20, 0))

name_entry = Entry(entries_frame)
name_entry.pack(pady=padding_y)
address_entry = Entry(entries_frame)
address_entry.pack(pady=padding_y)
phone_entry = Entry(entries_frame)
phone_entry.pack(pady=padding_y)
email_entry = Entry(entries_frame)
email_entry.pack(pady=padding_y)
birthday_entry = Entry(entries_frame)
birthday_entry.pack(pady=padding_y)

labels_frame = Frame(right_side_frame)
labels_frame.pack(side=LEFT)

name_label = Label(labels_frame, text='Name: ')
name_label.pack(pady=padding_y)
address_label = Label(labels_frame, text='Address: ')
address_label.pack(pady=padding_y)
phone_label = Label(labels_frame, text='Phone: ')
phone_label.pack(pady=padding_y)
email_label = Label(labels_frame, text='Email: ')
email_label.pack(pady=padding_y)
birthday_label = Label(labels_frame, text='Birthday: ')
birthday_label.pack(pady=padding_y)

def open_the_file():
    global address_dictionary
    file_name = askopenfile(title='open a file to see the address book', defaultextension='.txt')
    if file_name:
        content = file_name.read()
        address_dictionary = eval(content)
        file_name_variable.set(os.path.basename(file_name.name))
        for i in address_dictionary:
            the_list.insert(END, i)
        

open_button = Button(window, text='Open', command=open_the_file)
open_button.place(x=300, y=50)

list_frame = Frame(window)
list_frame.place(x=0, y=100)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

def display_info(event):
    current_choice = the_list.curselection()
    the_name = the_list.get(current_choice)
    info_list = address_dictionary[the_name]
    if current_choice:
        info_window = Toplevel(window)
        the_text = f'{the_name}\n{info_list[0]}\n{info_list[1]}\n{info_list[2]}\n{info_list[3]}'
        info_label = Label(info_window, text=the_text, font=('Arial', 25))
        info_label.grid(row=0, column=0)


the_list = Listbox(list_frame, width=30, height=20, yscrollcommand=scrollbar.set)
the_list.bind('<<ListboxSelect>>', display_info)
the_list.pack(side=LEFT, padx=10)

scrollbar.config(command=the_list.yview)


file_name_variable = StringVar()
file_name_label = Label(window, textvariable=file_name_variable)
file_name_label.place(x=110, y=60)

def get_things():
    name = name_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    birthday = birthday_entry.get()
    return (name, [address, phone, email, birthday])

def clear_things():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    phone_entry.delete(0, END)
    birthday_entry.delete(0, END)

def get_and_clear():
    result = get_things()
    clear_things()
    return result



def add_thing():
    global address_dictionary
    name, things = get_things()
    if not name:
        showwarning(message='please enter a name')
    else:
        clear_things()
    address_dictionary[name] = things
    if name not in the_list.get(0, END):
        the_list.insert(END, name)
    

update_add_button = Button(window, text='Update/Add', command=add_thing)
update_add_button.place(x=400, y=450)


def edit():
    current_item = the_list.curselection()
    if current_item:
        the_name = the_list.get(current_item)
        things = address_dictionary[the_name]
        clear_things()
        name_entry.insert(0, the_name)
        address_entry.insert(0, things[0])
        phone_entry.insert(0, things[1])
        email_entry.insert(0, things[2])
        birthday_entry.insert(0, things[3])
    else:
        showinfo(message='to edit an item you must select it.')
    
    

    

edit_button = Button(window, text='Edit', command=edit)
edit_button.place(x=50, y=450)

def delete_thing():
    current_item = the_list.curselection()
    if current_item:
        the_name = the_list.get(current_item)
        address_dictionary.pop(the_name)
        the_list.delete(current_item)
    else:
        showinfo(message='to delete an item you must select it.')

delete_button = Button(window, text='Delete', command=delete_thing)
delete_button.place(x=150, y=450)

def save_file():
    file_name = asksaveasfile(defaultextension='.txt', title='Save your address book')
    if file_name:
        print(address_dictionary, file=file_name)
    clear_things()
    the_list.delete(0, END)
    address_dictionary.clear()

save_button = Button(window, text='Save', width=20, command=save_file)
save_button.place(x=180, y=485)


window.mainloop()