import pgzrun
import random

speed = 5

paper_bag = Actor("paper bag")


trash = []
trash.append(Actor("plastic bag"))

WIDTH = 1000
HEIGHT = 500
paper_bag.x = random.randint(0,WIDTH)
paper_bag.y = 0

current_trash = []

level = 0
for i in range (level+1):
    current_trash.append(random.choice(trash))
    


def update():
    global current_trash, level
    for i in current_trash:
        i.y += speed
    paper_bag.y += speed
    
    if paper_bag.y > HEIGHT:
        level+= 1
        current_trash.clear()
        for i in range (level+1):
            current_trash.append(random.choice(trash))
            current_trash[i].y = 0
            current_trash[i].x = random.randint(0,WIDTH)
        paper_bag.x = random.randint(0,WIDTH)
        paper_bag.y = 0
    
def draw():
    screen.clear()
    paper_bag.draw()
    for i in current_trash:
        i.draw()


pgzrun.go()