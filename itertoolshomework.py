import random
import pgzrun
import math
import time


HEIGHT = WIDTH = 800

spaceship = Actor("spaceship.png")
mario = Actor("better mario.png")
mario.center = WIDTH/2, HEIGHT/2

def turn_ship():
    if game_over:
        return
    # global distance
    # x = random.randint(0,WIDTH)
    # y = random.randint(0,HEIGHT)
    # # angle = spaceship.angle_to(x,y)
    # # angle_to = 360*((angle+180)//2)
    # spaceship.target = x,y
    # target_angle = spaceship.angle_to(spaceship.target)
    target_angle = spaceship.angle_to(mario)#+random.uniform(-0.1,0.1)
    # distance = spaceship.distance_to(mario)
    # x_d = spaceship.x-mario.x
    # y_d = spaceship.y-mario.y
    # distance = math.sqrt(x_d*x_d + y_d*y_d)
    
    
    # # print(distance)
    # x = math.sin(target_angle)*distance
    # y = math.cos(target_angle)*distance
    spaceship.target = mario.x, mario.y
    # print(x,y)
    
    
    # print(spaceship.target)
    # print("turn ship")
    target_angle += 360*((spaceship.angle-target_angle+180)//360)-90
    animate(spaceship,
            angle = target_angle,
            duration = 0.4,
            on_finished=move_ship)


def move_ship():
    if game_over:
        return

    # print("move ship")
    animate(spaceship,
            tween="accel_decel",
            duration=spaceship.distance_to(spaceship.target)/400,
            pos = spaceship.target,
            on_finished=turn_ship)
    print("hello")
    
game_over = False
# time.sleep(5)
turn_ship()
# clock.schedule_interval(move_block, 2)




def update():
    global game_over
    if game_over:
        return
    if keyboard.a:
        mario.x -= 10
    if keyboard.d:
        mario.x += 10
    if keyboard.w:
        mario.y -= 10
    if keyboard.s:
        mario.y += 10
    
    if mario.x > WIDTH:
        mario.x = WIDTH
    if mario.x < 0:
        mario.x = 0
    if mario.y > HEIGHT:
        mario.y = HEIGHT
    if mario.y < 0:
        mario.y = 0
    
    # print(f"distance: {distance}")
    print(f"target: {spaceship.target}")
    print(f"mario: {mario.center}")
    if mario.colliderect(spaceship):
        print("game over!")
        game_over = True


    if spaceship.x > WIDTH:
        spaceship.x = WIDTH
    if spaceship.x < 0:
        spaceship.x = 0
    if spaceship.y > HEIGHT:
        spaceship.y = HEIGHT
    if spaceship.y < 0:
        spaceship.y = 0



halfwidth = WIDTH/2
halfheight = HEIGHT/2
def draw():
    screen.fill("black")

    spaceship.draw()
    mario.draw()

    if game_over:
        screen.draw.text("Game Over!", center=(halfwidth, halfheight), color="red", fontsize=70)
    
pgzrun.go()