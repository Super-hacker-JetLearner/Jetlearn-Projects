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

current_question_number = 0
current_question = questions[0]
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
time_out = False
def update():
    global time_left, current_question, wrong_answer, time_out, quiz_done
    if moving_box.right < 0:
        moving_box.x = WIDTH
        
    moving_box.x -= 5

    time_left = 3 - (time.time()-the_time)
    if time_left <= 0:
        current_question = ["Time has run out!", "-", "-", "-", "-", 5]
        time_left = 0
        time_out = time.time()
        # time_out = True
        quiz_done = True
        print("yes")
        
    if wrong_answer:
        if time.time() - wrong_answer > 1:
            wrong_answer = None
            
    # if time_out:
    #     if time.time() - time_out > 1:
    #         time_out = None
    #         quiz_done = True
    # if time_out:
    #     if time.time() - time_out > 1:
    #         pass
            # time_out = False
            # quiz_done = True
            # print("yes")
    
quiz_done = False
correct_questions = 0
wrong_answer = None
def on_mouse_down(pos):
    global current_question_number, current_question, questions, time_left, the_time, quiz_done, correct_questions, wrong_answer
    if time_out:
        return
    for i in range(len(answer_boxes)):
        if answer_boxes[i].collidepoint(pos):
            if int(current_question[5])-1 == i:
                correct_questions += 1
            else:
                print("wrong answer!")
                wrong_answer = time.time()
                
            try:
                current_question = questions[current_question_number+1]
            except:
                quiz_done = True
            current_question_number += 1
            time_left = 10
            the_time = time.time()

    if skip_box.collidepoint(pos):
        print("skip")
        try:
            current_question = questions[current_question_number+1]
        except:
            quiz_done = True
        
        current_question_number += 1
        time_left = 10
        the_time = time.time()

def draw():
    global quiz_done, current_question
    screen.fill("black")
    for i in answer_boxes:
        screen.draw.filled_rect(i, "orange")
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.filled_rect(moving_box, "red")
    screen.draw.textbox(f"{current_question_number+1} out of {len(questions)}", moving_box, color = (0,0,0), shadow = (0.5, 0.5), scolor = "yellow")
    screen.draw.filled_rect(timer_box, "blue")
    screen.draw.textbox(f"{round(time_left)}", timer_box, color=(0,0,0), shadow=(0.5, 0.5), scolor = "yellow")
    screen.draw.filled_rect(skip_box, "green")
    screen.draw.textbox("SKIP", skip_box, color=(0,0,0), angle = 90, shadow = (0.5, 0.5), scolor = "yellow")

    if wrong_answer:
        screen.draw.text("Wrong answer!", center=(600,400), color="red", fontsize=70)
        
    if time_out:
        screen.draw.text("Time out!", center=(600,400), color="red", fontsize=70)
        current_question = ["Time has run out!", "-", "-", "-", "-", 5]

        draw_questions(current_question)
        # delete this because draw does not work until the end
        # time.sleep(5)
    else:
        draw_questions(current_question)
    if time_out:
        print("time out")
        if time.time() - time_out > 1:
            print("more time")
            if quiz_done:
                print("quiz done")
                screen.fill("black")
                screen.draw.text(f"you got {correct_questions} out of {len(questions)} questions correct!", center=(600,400), color = "white", fontsize=70)
        

        
pgzrun.go()