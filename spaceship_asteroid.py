import pgzrun
import time
import random
import math

WIDTH = 1200
HEIGHT = 800
spaceship = Actor("spaceship.png")
appear_rate = (1,2)
asteroid_speed = 5

asteroids = []

halfheight = HEIGHT/2
halfwidth = WIDTH/2
def make_direction(x,y):
    direction = math.atan2(y-halfheight, x-halfwidth)
    


def make_asteroid():
    xy = random.choice(["x", "y"])
    asteroid = Actor("asteroid.png")
    if xy == "x":
        asteroid.x = random.choice([0, WIDTH])
        asteroid.y = random.randint(0,HEIGHT)
    else:
        asteroid.y = random.choice([0,HEIGHT])
        asteroid.x = random.randint(0,WIDTH)
        
        
    asteroid.xv = 0
    asteroid.yv = 0
    asteroids.append(asteroid)
        

the_time = time.time()
asteroid_time = random.uniform(appear_rate[0], appear_rate[1])

def update():
    global the_time, asteroid_time
    if time.time() - the_time > asteroid_time:
        make_asteroid()
        the_time = time.time()
        asteroid_time = random.uniform(appear_rate[0], appear_rate[1])

def draw():
    spaceship.draw()
    for i in asteroids:
        i.draw()
pgzrun.go()