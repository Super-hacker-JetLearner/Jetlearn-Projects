from tkinter import *
from tkinter.colorchooser import askcolor

class Paint():
    def __init__(self):
        self.window = Tk()
        self.window.geometry('1000x1000')
        self.window.focus_force()
        
        self.color = 'black'

        self.menu_frame = Frame(self.window, background="#cccccc", borderwidth=10)
        self.menu_frame.grid(row=0, column=0, sticky=N+W+S+E)
        Grid.rowconfigure(self.window, 0, weight = 1, minsize=120)
        Grid.columnconfigure(self.window, 0, weight = 1)

        pady = 30
        font = ('Arial', 25)

        self.pen_button = Button(self.menu_frame, text='pen', font=font, command=self.on_pen_press)
        self.active_button = self.pen_button
        self.pen_button.grid(row=0, column=0, pady=pady)


        self.brush_button = Button(self.menu_frame, text='brush', font=font, command=self.on_brush_press)
        self.brush_button.grid(row=0, column=1, pady=pady)

        self.color_button = Button(self.menu_frame, text='color', font=font, command=self.on_color_press)
        self.color_button.grid(row=0, column=2, pady=pady)

        self.eraser_button = Button(self.menu_frame, text='eraser', font=font, command=self.on_eraser_press)
        self.eraser_button.grid(row=0, column=3, pady=pady)
        


        Grid.rowconfigure(self.menu_frame, 0, weight = 1)
        for i in range (5):
            Grid.columnconfigure(self.menu_frame, i, weight = 1)
        self.slider_var = IntVar()
        self.slider = Scale(self.menu_frame, from_=1, to=50, orient=HORIZONTAL, length=200, variable=self.slider_var)
        self.slider.grid(row=0, column=4, pady=pady)

        self.canvas = Canvas(self.window, height=900, background='white')
        self.canvas.grid(row=1, column=0, sticky=N+W+S+E)
        Grid.rowconfigure(self.window, 1, weight = 1)

        self.oldx = None
        self.oldy = None
        self.eraser_on = False
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        

        
    def on_pen_press(self):
        self.on_button_press(self.pen_button)
    def on_brush_press(self):
        self.on_button_press(self.brush_button)
    def on_color_press(self):
        self.on_button_press(self.color_button)
    def on_eraser_press(self):
        self.on_button_press(self.eraser_button, eraser=True)

    def on_button_press(self, button:Button, eraser:bool=False):
        self.active_button.config(relief=RAISED)
        button.config(relief=SUNKEN)
        self.active_button = button
        if button == self.color_button:
            self.color = askcolor(color=self.color)[1]
        if eraser:
            if self.eraser_on:
                self.eraser_on = False
            else:
                self.eraser_on = True
        else:
            self.eraser_on = False
        
    
    def paint(self, event):
        if self.oldx and self.oldy:
            if not self.eraser_on:
                self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill=self.color, width=self.slider_var.get(),  capstyle=ROUND)
            else:
                self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill='white', width=self.slider_var.get(),  capstyle=ROUND)
        self.oldx = event.x
        self.oldy = event.y
    def reset(self, event):
        self.oldx = None
        self.oldy = None

paint_screen = Paint()
paint_screen.window.mainloop()