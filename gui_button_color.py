import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('450x300')


style = ttk.Style()
style.configure('red_button.TButton', background='green')
style.map('red_button.TButton', background=[('active', '#0f67f5'), ('pressed', '#f50f0f')], foreground=[('disabled', 'gray')])

button = ttk.Button(root, text='click me', style='red_button.TButton')
button.pack(side='top')

root.mainloop()