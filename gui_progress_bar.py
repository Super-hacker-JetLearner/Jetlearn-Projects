from tkinter import *
from tkinter.ttk import *
import time

window = Tk()
window.geometry('450x300')
window.title('progress bar')

progress_bar = Progressbar(window, orient='horizontal', length=100, mode='determinate')
progress_bar.pack(side='top')


def start_bar():
    
    progress_bar['value'] += 20
    window.update_idletasks()
    window.update()
    time.sleep(1)

button = Button(window, text='start', command=start_bar)
button.pack(side='left')

window.mainloop()