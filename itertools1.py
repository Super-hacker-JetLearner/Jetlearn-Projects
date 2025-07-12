import pgzrun
import random
import itertools


WIDTH = 800
HEIGHT = 800


block_positions = [(50,750),
                   (50,50),
                   (750,50),
                   (750,750)]

block_positions = itertools.cycle(block_positions)

block = Actor("mario wall.png")
spaceship = Actor("spaceship.png")
spaceship.center = WIDTH/2, HEIGHT/2

def move_block():
    animate(block,
            "bounce_end",
            duration=2,
            pos=next(block_positions))


def turn_ship():
    x = random.randint(200,500)
    y = random.randint(200,500)
    # angle = spaceship.angle_to(x,y)
    # angle_to = 360*((angle+180)//2)
    spaceship.target = x,y
    target_angle = spaceship.angle_to(spaceship.target)
    
    print("turn ship")
    target_angle += 360*((spaceship.angle-target_angle+180)//360)-90
    animate(spaceship,
            angle = target_angle,
            duration = 0.4,
            on_finished=move_ship)


def move_ship():
    print("move ship")
    animate(spaceship,
            tween="accel_decel",
            duration=spaceship.distance_to(spaceship.target)/200,
            pos = spaceship.target,
            on_finished=turn_ship)
    

move_block()
turn_ship()
clock.schedule_interval(move_block, 2)





def draw():
    screen.fill("black")
    block.draw()
    spaceship.draw()

pgzrun.go()