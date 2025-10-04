from tkinter import *
import math

# window initilisation

window = Tk()
window.geometry('400x700')
window.focus_force()
window['background'] = 'light grey'

warning_label = Label(window, text='Warning: Calculator does not use bodmass,\nit goes from left to right!', font=('Arial', 20))
warning_label.pack()

equation_label = Label(window, text='Equation:', font=('Arial', 20))
equation_label.pack(pady=(20, 0))

equation_text = Text(window, font=('Arial', 20), width=30, height=3)
equation_text.pack(pady=(10, 0))

result_label = Label(window, text='Result:', font=('Arial', 20))
result_label.pack(pady=(20, 0))

result_text = Text(window, font=('Arial', 20), width=30, height=2)
result_text['state'] = DISABLED
result_text.pack(pady=(10, 0))


ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else float('inf')  # safe division
}

def calculate(text:str):
    global ops
    result:float = 0
    this_num = ''
    text = text.replace(' ', '')
    text = text.replace('\n', '')
    prev_op = '+'
    for char in text:
        print(char)
        if char.isdigit() or char == '.':
            this_num += char
            print(f'char isnum and this_num is {this_num}')
        
        if char in ops:
            print(f'char is in ops and is {char}')
            print(f'equation: {result} {prev_op} {this_num}')
            result = ops[prev_op](result, float(this_num))
            if math.isnan(result):
                print('error! not a number!')
                return 'error! not a number!'
            this_num = ''
            prev_op = char


    print('end')
    print(f'equation: {result} {prev_op} {this_num}')
    result = ops[prev_op](result, int(this_num))

    if math.isnan(result):
        print('error! not a number!')
        return 'error! not a number!'
        
    return result


def on_button_click():
    text = equation_text.get("1.0", "end-1c")
    result = calculate(text)
    result_text['state'] = NORMAL
    result_text.delete("1.0", END)
    result_text.insert("1.0", str(result))
    result_text['state'] = DISABLED

    


calculate_button = Button(window, font=('Arial', 30), text='Calculate', command=on_button_click)
calculate_button.pack(pady=(50, 0))





        


window.mainloop()