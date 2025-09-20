from tkinter import *
import random
from tictactoe import find_best_move

print('imported')

root = Tk()
root.geometry('200x300')
root.focus_force()

scores:dict = {'x':0, 'o':0}


def change_score(increase:str=None):
    global scores, score_label
    if increase == 'x':
        scores['x'] += 1
    elif increase == 'o':
        scores['o'] += 1
    score_label.config(text=f'Score - X:{scores['x']} | O:{scores['o']}')
    
def reset_score():  
    global scores, score_label
    scores['x'] = 0
    scores['o'] = 0
    try:
        score_label.config(text=f'Score - X:0 | O:0')
    except:
        pass
    

select_label = Label(root, text='Select Mode', font=('Arial', 30))
select_label.pack(pady=30)

state = None
player = 'x'

def change_player():
    global player, player_label
    if player == 'x':
        new_value = 'O'
        player = 'o'
    else:
        new_value = 'X'
        player = 'x'
    player_label.config(text=f'Player: {new_value}')
    
def set_player(the_player:str='x'):
    global player, player_label
    player = the_player
    try:
        player_label.config(text=f'Player: {player}')
    except:
        pass

def multiplayer():
    global state, player
    state = 'single'
    make_board(True)
def single_player():
    global state, player
    state = 'multi'
    # do multiplayer stuff

single_button = Button(root, text='Single Player', font=('Arial', 20), command=single_player)
single_button.pack(pady=15)
multiple_button = Button(root, text='Multiplayer', font=('Arial', 20), command=multiplayer)
multiple_button.pack(pady=15)
reset_button = Button(root, text='reset score', font=('Arial', 20), command=reset_score)
reset_button.pack(pady=15)

disabled = False

print('done setup')

def on_button_click(index:tuple):
    global buttons, player, disabled
    print('clicked')
    print(index)
    if state == 'single':
        if buttons[index[0]][index[1]]['text'] is '' and not disabled:
            buttons[index[0]][index[1]].config(text=player)
            change_player()
            if check_win('x'):
                print('x won!')
                change_score('x')
                disabled = True
            elif check_win('o'):
                print('o won!')
                change_score('o')
                disabled = True
            elif check_draw():
                print('draw')
                disabled = True
    elif state == 'multi':
        if player == 'o':
            if buttons[index[0]][index[1]]['text'] is '' and not disabled:
                buttons[index[0]][index[1]].config(text=player)
                if check_win('x'):
                    print('x won!')
                    change_score('x')
                    disabled = True
                elif check_win('o'):
                    print('o won!')
                    change_score('o')
                    disabled = True
                elif check_draw():
                    print('draw')
                    disabled = True
                    
                make_move()
                
                if check_win('x'):
                    print('x won!')
                    change_score('x')
                    disabled = True
                elif check_win('o'):
                    print('o won!')
                    change_score('o')
                    disabled = True
                elif check_draw():
                    print('draw')
                    disabled = True
        
def check_win(player):
    for row in range (3):
        if buttons[row][0]['text'] == player and buttons[row][1]['text'] == player and buttons[row][2]['text'] == player:
            return True
    
    for column in range (3):
        if buttons[0][column]['text'] == player and buttons[1][column]['text'] == player and buttons[2][column]['text'] == player:
            return True
        
    if buttons[0][0]['text'] == player and buttons[1][1]['text'] == player and buttons[2][2]['text'] == player:
        return True
    if buttons[2][0]['text'] == player and buttons[1][1]['text'] == player and buttons[0][2]['text'] == player:
        return True
    
def check_draw():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == '':
                return False
    return True


def make_board(multi:str=False):
    global player_label, score_label, buttons, disabled
    disabled = False
    window = Toplevel(root)
    window.geometry('600x600')
    buttons = []
    score_label = Label(window, font=('Arial', 20))
    player_label = Label(window, font=('Arial', 20))
    player_label.config(text=f'Player: X')
    if multi:
        set_player('o')
    else:
        set_player('x')
    change_score()
    score_label.grid(row=0, column=0, sticky=None)
    player_label.grid(row=0, column=2, sticky=None)
    
    Grid.rowconfigure(window, 0, weight=0)
    for row in range(1, 4):
        Grid.rowconfigure(window, row, weight=1)
        buttons.append([])
        for column in range (3):
            Grid.columnconfigure(window, column, weight=1, uniform=True)
            button = Button(window, command=lambda index = (row-1, column): on_button_click(index), font=('Arial', 50))
            buttons[-1].append(button)
            button.grid(row=row, column=column, sticky=N+E+S+W)


def make_move():
    global buttons
    number_board = buttons
    for row in range(3):
        for column in range(3):
            if number_board[row][column]['text'] == 'x':
                number_board[row][column] = 1
            elif number_board[row][column]['text'] == 'o':
                number_board[row][column] = 2
            elif number_board[row][column]['text'] == '':
                number_board[row][column] = 0
                
    new_board = find_best_move(number_board)
    for row in range(3):
        for column in range(3):
            if new_board[row][column] == 1:
                buttons[row][column]['text'] = 'x'
            elif new_board[row][column] == 2:
                buttons[row][column]['text'] = 'o'
            elif new_board[row][column] == 0:
                buttons[row][column]['text'] = ''
    



            

root.mainloop()