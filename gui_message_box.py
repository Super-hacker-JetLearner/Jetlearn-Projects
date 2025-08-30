from tkinter import *
from tkinter import messagebox

from tkinter.messagebox import *
# window = Tk()
# window.geometry('500x500')


messagebox.showwarning('title', 'this is a message')

messagebox.askquestion(message='do you want to save it?')

messagebox.askokcancel(message='do you want to cancel navigation?')

messagebox.askretrycancel(message='do you want to retry?')
messagebox.askquestion(message='what do you want to do?', default=[messagebox.RETRY, messagebox.IGNORE])
# messagebox.