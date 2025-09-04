from tkinter import *
from random import randint

window = Tk()
window.title('Rock Paper Scissors')
window.geometry('800x500')

# use win_lose_array[computer][person]
win_lose_array = [['Tie', 'Lose', "Win"],
                  ['Win', 'Tie', 'Lose'],
                  ['Lose', 'Win', 'Tie']]

# rock_button = Button(window, text='rock', font=('Arial', 25))
# rock_button.place(x=300, y=300)

# paper_button = Button(window, text='paper', font=('Arial', 25))
# paper_button.place(x=400, y=300)

# scissors_button = Button(window, text='scissors', font=('Arial', 25))
# scissors_button.place(x=500, y=300)
computer_choice_text = 'Computer Chose: '
you_choice_text = 'You Chose: '
computer_score_text = 'Computer Score: '
you_score_text = 'Your Score: '

computer_chose_variable = StringVar(value=computer_choice_text)
you_choice_variable = StringVar(value=you_choice_text)
computer_score_variable = StringVar(value=computer_score_text+'0')
you_score_variable = StringVar(value=you_score_text+'0')
you_choice_label_variable = StringVar(value='You Chose: ')




def person_choice():
    computer_result = randint(0,2)
    computer_chose_variable.set(computer_chose_variable.get()+str(computer_result))
    person_result = you_choice_variable.get()
    you_choice_variable.set(you_choice_variable.get())
    winner = win_lose_array[computer_result][int(person_result)]
    if winner == 'Tie':
        print('tie')
    elif winner == 'Lose':
        print('lose')
        prev_text = computer_score_variable.get()
        prev_text_list = prev_text.rsplit(' ', 1)
        print(prev_text_list)
        prev_text_text = prev_text_list[0]
        prev_text_value = int(prev_text_list[1])
        prev_text_value += 1
        computer_score_variable.set(prev_text_text+' '+str(prev_text_value))
        
    elif winner == 'Win':
        print('win')
        prev_text = you_score_variable.get()
        prev_text_list = prev_text.rsplit(' ', 1)
        print(prev_text_list)
        prev_text_text = prev_text_list[0]
        prev_text_value = int(prev_text_list[1])
        prev_text_value += 1
        you_score_variable.set(prev_text_text+' '+str(prev_text_value))
        

buttons = Radiobutton()
values = {"rock" : "0",
            "paper" : "1",
            "scissors" : "2"}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
radio_buttons = []
for (text, value) in values.items():
    radio_button = Radiobutton(window, text = text, variable = you_choice_variable, 
                value = value, indicator = 0,
                background = "light blue", command=person_choice)
    radio_button.pack(fill = X, ipady = 5)
    radio_buttons.append(radio_button)





bottom_frame = Frame(window)
bottom_frame.pack(side=BOTTOM)
choice_frame = Frame(bottom_frame)
choice_frame.pack(side=LEFT)
computer_chose = Label(choice_frame, text='Computer Chose: ', font=('Arial', 25), textvariable=computer_chose_variable)
computer_chose.pack(padx=10)
you_chose = Label(choice_frame, text='You Chose: ', font=('Arial', 25), textvariable=you_choice_label_variable)
you_chose.pack(padx=10)

score_frame = Frame(bottom_frame)
score_frame.pack(side=RIGHT)
computer_score = Label(score_frame, text='Computer Score: 0', font=('Arial', 25), textvariable=computer_score_variable)
computer_score.pack(padx=10)
you_score = Label(score_frame, text='Your Score: 0', font=('Arial', 25), textvariable=you_score_variable)
you_score.pack(padx=10)



window.mainloop()