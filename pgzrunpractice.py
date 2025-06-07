import pgzrun
import random


WIDTH = 300
HEIGHT = 300


TITLE = "pgzrun squares"


def draw_square():
    width = 300
    height = 300
    for i in range (30):
        rectangle = Rect((0,0), (width, height))
        rectangle.center = 150,150
        screen.draw.rect(rectangle, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        width -= 10
        height -= 10


def draw_circle():
    radius = 220
    for i in range (40):
        screen.draw.filled_circle((150,150), radius, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        radius -= 10


def draw_rectangle():
    width = 300
    height = 0
    for i in range (30):
        rectangle = Rect((0,0), (width, height))
        rectangle.center = 150,150
        screen.draw.rect(rectangle, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        width -= 10
        height += 10


def draw():

    draw_circle()
    draw_square()
    draw_rectangle()

pgzrun.go()