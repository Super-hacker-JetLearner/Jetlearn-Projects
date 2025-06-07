import pgzrun
import random


WIDTH = 300
HEIGHT = 300

alien = Actor("alien")

alien.x = random.randint(0,300)
alien.y = random.randint(0,300)



def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("ow")
        alien.x = random.randint(0,300)
        alien.y = random.randint(0,300)
    else:
        print("you missed me!!!!")

def draw():
    # screen.clear()
    screen.fill(color = (255,0,255))
    alien.draw()



pgzrun.go()