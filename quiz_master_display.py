import pgzrun
import time
import random

WIDTH = 1200
HEIGHT = 800


questions = []
with open("questions.txt", "r") as f:
    for i in f.readlines():
        questions.append(i.strip().split(","))
        
random.shuffle(questions)

current_question = 0
def draw_questions(question):
    screen.draw.textbox(f"{question[0]}", question_box, color = (0,0,0), shadow = (0.5, 0.5), scolor = "yellow")
    for i in range(4):
        screen.draw.textbox(f"{question[i+1]}", answer_boxes[i], color= (0,0,0), shadow = (0.5, 0.5), scolor = "yellow")


answer_boxes = [Rect(0,0,400,200), Rect(0,0,400,200), Rect(0,0,400,200), Rect(0,0,400,200)]

answer_boxes[0].move_ip(0,200)
answer_boxes[1].move_ip(0, 500)
answer_boxes[2].move_ip(500, 200)
answer_boxes[3].move_ip(500, 500)
question_box = Rect(0,100, 800,100)
moving_box = Rect(0,0, 800, 100)
timer_box = Rect(0,0, 200, 200)
timer_box.topright = WIDTH, 0
skip_box = Rect(0,0,200,400)
skip_box.topright = WIDTH, 200

the_time = time.time()
time_left = 10
def update():
    global time_left
    if moving_box.right < 0:
        moving_box.x = WIDTH
        
    moving_box.x -= 5

    time_left = 10 - (time.time()-the_time)
    if time_left <= 0:
        for i in answer_boxes:
            pass

def draw():
    screen.fill("black")
    for i in answer_boxes:
        screen.draw.filled_rect(i, "orange")
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.filled_rect(moving_box, "red")
    screen.draw.textbox(f"{current_question+1} out of {len(questions)}", moving_box, color = (0,0,0), shadow = (0.5, 0.5), scolor = "yellow")
    screen.draw.filled_rect(timer_box, "blue")
    screen.draw.textbox(f"{round(time_left)}", timer_box, color=(0,0,0), shadow=(0.5, 0.5), scolor = "yellow")
    screen.draw.filled_rect(skip_box, "green")
    screen.draw.textbox("SKIP", skip_box, color=(0,0,0), angle = 90, shadow = (0.5, 0.5), scolor = "yellow")
    draw_questions(questions[0])
pgzrun.go()