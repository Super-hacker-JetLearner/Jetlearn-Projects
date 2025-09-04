from tkinter import *

window = Tk()

screen_width = 500
screen_height = 300

window.geometry(f'{screen_width}x{screen_height}')

conversions = {'rupee:dollar':0.011}

def bad_number_message():
    def close(event=None):
        bad_number_label.destroy()
    bad_number_label = Label(window, text='Error!', background='red', font=('Arial', 25))
    bad_number_label.place(x=200, y=150)
    bad_number_label.bind('<Button-1>', close)
    bad_number_label.after(3000, close)


def convert():
    try:
        value = int(first_frame_entry.get())
    except:
        bad_number_message()
        return
    if value == "":
        bad_number_message()
        return
    converted_value = value * conversions['rupee:dollar']
    first_frame.destroy()
    answer_screen(converted_value=converted_value)
    
def go_back():
    second_frame.destroy()
    start_screen()
    


def start_screen():
    global first_frame, first_frame_entry
    first_frame = Frame(window, width=screen_width, height=screen_height)
    first_frame.place(x=0,y=0)
    first_frame_label = Label(first_frame, text='Rupee -> Dollar', font=('Arial', 25), foreground="grey")
    first_frame_label.place(x=200, y=0)
    first_frame_entry = Entry(first_frame)
    first_frame_entry.place(x=250, y=70)
    first_frame_label2 = Label(first_frame, text='Enter money in Rupee:')
    first_frame_label2.place(x=100, y=70)
    first_frame_button = Button(first_frame, text='Convert', command=convert)
    first_frame_button.place(x=150, y=200)
    
    
def answer_screen(converted_value):
    global second_frame
    second_frame = Frame(window, width=screen_width, height=screen_height)
    second_frame.place(x=0,y=0)
    answer_label = Label(second_frame, text=f'result: {converted_value}')
    answer_label.place(x=200, y=150)
    back_button = Button(second_frame, text='Back', command=go_back)
    back_button.place(x=50,y=50)
    
    
start_screen()

window.mainloop()