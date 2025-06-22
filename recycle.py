import pgzrun
import random

speed = 2
acceleration = 0.8

paper_bag = Actor("paper bag")


trash_names = ["plastic bag.png", "plastic bottle.png", "battery.png"]


WIDTH = 1000
HEIGHT = 500
paper_bag.x = random.randint(0,WIDTH)
paper_bag.y = 0

current_trash = []
stop = False  # Flag to stop the game

level = 0
for i in range (level+1):
    current_trash.append(Actor(random.choice(trash_names)))


def draw_random_trash(trash, paper_bag):
    trash.append(paper_bag)
    random.shuffle(trash)
    for i in range (len(trash)):
        trash[i].y = 0
        trash[i].x = i*(WIDTH/len(trash))+ (WIDTH/len(trash))/2
    trash.remove(paper_bag)



def on_mouse_down(pos):
    global current_trash, stop, paper_bag, level, speed, acceleration
    # Check if the game is stopped
    if stop:
        return
    
    if paper_bag.collidepoint(pos):
        print("You caught the paper bag!")
        current_trash.clear()
        level += 1
        for i in range(level + 1):
            current_trash.append(Actor(random.choice(trash_names)))
        draw_random_trash(current_trash, paper_bag)
        speed += acceleration  # Increase speed when paper bag is caught
    else:
        for i in current_trash:
            if i.collidepoint(pos):
                print("game over")
                screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=60, color="red")
                stop = True  # Stop the game if trash is clicked

def update():
    global current_trash, level, speed, acceleration, stop
    if stop:
        return

    # speed += acceleration
    for i in current_trash:
        i.y += speed
    paper_bag.y += speed
    
    if paper_bag.y > HEIGHT:
        # level+= 1
        # current_trash.clear()
        # for i in range (level+1):
        #     current_trash.append(Actor(random.choice(trash_names)))
        print("game over")
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=60, color="red")
        stop = True  # Stop the game when paper bag goes off the screen
        
        draw_random_trash(current_trash, paper_bag)
        
        # paper_bag.x = random.randint(0,WIDTH)
        # paper_bag.y = 0
    if level == 7:
        print("You win!")
        screen.draw.text("You win!", center=(WIDTH/2, HEIGHT/2), fontsize=60, color="green")
        stop = True  # Stop the game when level reaches 7
    
def draw():
    if stop:
        return  # Do not draw anything if the game is stopped
    screen.clear()
    paper_bag.draw()
    for i in current_trash:
        i.draw()


pgzrun.go()