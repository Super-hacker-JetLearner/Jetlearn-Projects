from tkinter import *
import random
import math

window = Tk()
window.resizable(False, False)
WIDTH = 1000
HEIGHT = 800

window.geometry(f'{WIDTH}x{HEIGHT}')
window['background'] = 'green'
window.focus_force()

canvas = Canvas(window, background='black')
canvas.grid(row=0, column=0, sticky=N+S+E+W)

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

midline = canvas.create_line(500, 0, 500, 800, width=3, fill='white')
mid_circle_half_radius = 75
mid_circle = canvas.create_oval(500-mid_circle_half_radius, 400-mid_circle_half_radius, 500+mid_circle_half_radius, 400+mid_circle_half_radius, outline='white', width=3)
score = [0,0]
score_text = canvas.create_text(500, 50, text='0 : 0', fill='white', font=('Arial', 40, 'bold'))

ball_color = "#FFB300"

ball_radius = 40
ball = canvas.create_oval(500-ball_radius/2, 400-ball_radius/2, 500+ball_radius/2, 400+ball_radius/2, fill=ball_color)

ball_velocity = [0, 0]

ball_speed = 5
direction = random.uniform(0, math.pi*2)

ball_velocity[0] = math.cos(direction)*ball_speed
ball_velocity[1] = math.sin(direction)*ball_speed

ball_pos = [500, 400]


paddle_size = [20, 200]
paddle_pos = [30, 300]
paddle1_color = "#44FF00"
paddle2_color = "#FF0000"

paddle1 = canvas.create_rectangle(paddle_pos[0], paddle_pos[1], paddle_size[0]+paddle_pos[0], paddle_size[1]+paddle_pos[1], fill=paddle1_color)
paddle2 = canvas.create_rectangle(WIDTH-paddle_pos[0], paddle_pos[1], WIDTH-(paddle_size[0]+paddle_pos[0]), paddle_size[1]+paddle_pos[1], fill=paddle2_color)

paddle1_y = 300
paddle2_y = 300

paddle1_velocity = 0
paddle2_velocity = 0

frame_rate = 20 # milliseconds
speed = 20 # per frame_rate


def on_key_down(event:Event):
    print(event.keysym)
    global paddle1_velocity, paddle2_velocity
    if event.keysym == 'w':
        paddle1_velocity = -1
    if event.keysym =='s':
        paddle1_velocity = 1
    
    if event.keysym == 'Up':
        paddle2_velocity = -1
    if event.keysym == 'Down':
        paddle2_velocity = 1
        
        
def on_key_up(event:Event):
    print(event.keysym)
    global paddle1_velocity, paddle2_velocity
    if event.keysym == 'w' and paddle1_velocity == -1:
        paddle1_velocity = 0
    if event.keysym == 's' and paddle1_velocity == 1:
        paddle1_velocity = 0
    
    if event.keysym == 'Up' and paddle2_velocity == -1:
        paddle2_velocity = 0
    if event.keysym == 'Down' and paddle2_velocity == 1:
        paddle2_velocity = 0
    

def move_paddles():
    global paddle1_y, paddle2_y
    paddle1_y += speed * paddle1_velocity
    if paddle1_y + paddle_size[1] > HEIGHT:
        paddle1_y = HEIGHT-paddle_size[1]
    if paddle1_y < 0:
        paddle1_y = 0
        
    canvas.moveto(paddle1, paddle_pos[0], paddle1_y)
    
    paddle2_y += speed * paddle2_velocity
    if paddle2_y + paddle_size[1] > HEIGHT:
        paddle2_y = HEIGHT-paddle_size[1]
    if paddle2_y < 0:
        paddle2_y = 0
    
    canvas.moveto(paddle2, WIDTH-(paddle_size[0]+paddle_pos[0]), paddle2_y)
    

    

canvas.bind_all('<KeyPress-w>', on_key_down)
canvas.bind_all('<KeyPress-s>', on_key_down)
canvas.bind_all('<KeyRelease-s>', on_key_up)
canvas.bind_all('<KeyRelease-w>', on_key_up)

canvas.bind_all('<KeyPress-Up>', on_key_down)
canvas.bind_all('<KeyPress-Down>', on_key_down)
canvas.bind_all('<KeyRelease-Down>', on_key_up)
canvas.bind_all('<KeyRelease-Up>', on_key_up)

def move_ball():
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]
    if ball_pos[1] < 0:
        ball_pos[1] = 0
        ball_velocity[1] *= -1
    if ball_pos[1] + ball_radius > HEIGHT:
        ball_pos[1] = HEIGHT-ball_radius
        ball_velocity[1] *= -1
    if ball_pos[0] < 0:
        score[1] += 1
        canvas.itemconfig(score_text, text=f'{score[0]} : {score[1]}')
        reset_all()
        return True
    if ball_pos[0] > WIDTH:
        score[0] += 1
        canvas.itemconfig(score_text, text=f'{score[0]} : {score[1]}')
        reset_all()
        return True
    
    
    if ball_pos[0] < paddle_pos[0] + paddle_size[0]:
        print('x')
        if ball_pos[1] > paddle1_y and ball_pos[1]+ball_radius < paddle1_y+paddle_size[1]:
            print('y')
            ball_pos[0] = paddle_pos[0]+paddle_size[0]
            ball_velocity[0] *= -1
            
    if ball_pos[0]+ball_radius > WIDTH-(paddle_pos[0]+paddle_size[0]):
        print('x')
        if ball_pos[1] > paddle2_y and ball_pos[1]+ball_radius < paddle2_y+paddle_size[1]:
            print('y')
            ball_pos[0] = WIDTH-(paddle_pos[0]+ball_radius+paddle_size[0])
            ball_velocity[0] *= -1
            
    
    canvas.moveto(ball, ball_pos[0], ball_pos[1])
    

def reset_all():
    global paddle1_y, paddle2_y, ball_velocity, ball_velocity, ball_pos
    paddle1_y = paddle_pos[1]
    paddle2_y = paddle_pos[1]
    
    direction = random.uniform(0, math.pi*2)
    ball_velocity[0] = math.cos(direction)*ball_speed
    ball_velocity[1] = math.sin(direction)*ball_speed
    ball_pos = [500, 400]
    canvas.after(2000, do_all)

def check_winner():
    if score[0] >= 1:
        print('player 1 won!')
        winner_text = canvas.create_text(500, 400, text='Player 1 won!', fill='green', font=('Arial', 100, 'bold'))
        return True
    if score[1] >= 1:
        print('player 2 won!')
        winner_text = canvas.create_text(500, 400, text='Player 2 won!', fill='red', font=('Arial', 100, 'bold'))
        return True



def do_all():
    move_paddles()
    if check_winner():
        return
    if move_ball():
        return
    canvas.after(20, do_all)

reset_all()


window.mainloop()