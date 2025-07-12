import pgzrun
import time
import random
import math
import pygame

WIDTH = 1200
HEIGHT = 800
spaceship = Actor("spaceship.png")
spaceship.center = WIDTH/2, HEIGHT/2
appear_rate = (0.5,1)
asteroid_speed = 0.5
projectile_speed = 10
spaceship_speed = 10
shoot_speed = 0.2
score = 0
knockback = 0.5
asteroid_health = 10
health = 3
game_over = False

asteroids = []

halfheight = HEIGHT/2
halfwidth = WIDTH/2
def make_direction(x,y):
    direction = math.atan2(y-spaceship.y, x-spaceship.x)
    # direction = actor.angle_to((halfwidth,halfheight))+180
    x_change = -math.cos(direction)*asteroid_speed
    y_change = -math.sin(direction)*asteroid_speed
    return (x_change, y_change)


def make_asteroid():
    xy = random.choice(["x", "y"])
    asteroid = Actor("asteroid.png")
    if xy == "x":
        asteroid.x = random.choice([0, WIDTH])
        asteroid.y = random.randint(0,HEIGHT)
    else:
        asteroid.y = random.choice([0,HEIGHT])
        asteroid.x = random.randint(0,WIDTH)
        
    
    x,y = make_direction(asteroid.x, asteroid.y)
    asteroid.xv = x
    asteroid.yv = y
    asteroid.health = asteroid_health

    asteroids.append(asteroid)
        


projectiles = []
last_shot = time.time()
def make_projectile(x,y,direction):
    projectile = Actor("bullet.png")
    projectile.center = x,y
    x_change = math.cos(direction)*projectile_speed
    y_change = math.sin(direction)*projectile_speed
    projectile.xv = x_change
    projectile.yv = y_change
    projectiles.append(projectile)

the_time = time.time()
asteroid_time = random.uniform(appear_rate[0], appear_rate[1])


prev_spaceship_pos = (100,100)
def update():
    global the_time, asteroid_time, last_shot, score, prev_spaceship_pos, health, game_over
    
    if game_over:
        return
    
    if keyboard.a:
        spaceship.x -= spaceship_speed
    if keyboard.d:
        spaceship.x += spaceship_speed
    if keyboard.w:
        spaceship.y -= spaceship_speed
    if keyboard.s:
        spaceship.y += spaceship_speed
    
    if keyboard.SPACE or pygame.mouse.get_pressed()[0]:
        print("space")
        # print(pygame.mouse.get_pressed())
        if time.time() - last_shot > shoot_speed:
            mouse_pos = pygame.mouse.get_pos()
            mouse_angle = math.atan2(spaceship.y-mouse_pos[1], spaceship.x-mouse_pos[0])+math.pi
            print(mouse_angle)
            make_projectile(spaceship.x, spaceship.y, mouse_angle)
            last_shot = time.time()
    
    
    if spaceship.x < 0:
        spaceship.x = 0
    if spaceship.x > WIDTH:
        spaceship.x = WIDTH
    if spaceship.y < 0:
        spaceship.y = 0
    if spaceship.y > HEIGHT:
        spaceship.y = HEIGHT
    
    
    
    
    if time.time() - the_time > asteroid_time:
        make_asteroid()
        the_time = time.time()
        asteroid_time = random.uniform(appear_rate[0], appear_rate[1])
     
     
    # make_projectile(random.randint(0,WIDTH), random.randint(0,HEIGHT), random.randint(0,360))
    
    for i in asteroids:
        i.x += i.xv
        i.y += i.yv
    
    for i in projectiles:
        i.x += i.xv
        i.y += i.yv
    
    for i in projectiles:
        for j in asteroids:
            try:
                if i.colliderect(j):
                    # # print("if")
                    # score += 10
                    # # print("score")
                    # projectiles.remove(i)
                    # # print("projectiles")
                    # asteroids.remove(j)
                    # # print("yeah")
                    j.health -= 1
                    print("hit")
                    
                    direction = math.atan2(i.y-j.y, i.x-j.x)
                    x_change = math.cos(direction)*knockback
                    y_change = math.sin(direction)*knockback
                    j.xv -= x_change
                    j.yv -= y_change
                    projectiles.remove(i)
                    
                    if j.health <= 0:
                        # projectiles.remove(i)
                        asteroids.remove(j)
                        score += 10
                        print("destroyed")
            except:
                # print("no")
                pass

    
    for i in asteroids:
        for j in asteroids:
            try:
                if i != j:
                    if i.colliderect(j):
                        asteroid_direction = math.atan2(i.y-j.y, i.x-j.x)
                        i_total = math.sqrt(i.xv*i.xv + i.yv*i.yv)
                        j_total = math.sqrt(j.xv*j.xv + j.yv*j.yv)
                        total = i_total+j_total
                        half_total = total/2
                        i_x_change = -math.cos(-asteroid_direction)*half_total
                        i_y_change = -math.sin(-asteroid_direction)*half_total
                        i.xv = i_x_change
                        i.yv = i_y_change

                        j_x_change = -math.cos(asteroid_direction)*half_total
                        j_y_change = -math.sin(asteroid_direction)*half_total
                        j.xv = j_x_change
                        j.yv = j_y_change
                    
            
            except:
                pass

        
    for i in asteroids:
        if spaceship.colliderect(i):
            health -= 1
            asteroids.clear()
            spaceship.center = (halfwidth, halfheight)

    # if prev_spaceship_pos != spaceship.center:
    #     for i in asteroids:
    #         x,y = make_direction(i.x, i.y)
    #         i.xv = x
    #         i.yv = y
    #     prev_spaceship_pos = spaceship.center
    #     print("direction")
    # else:
    #     print("no direction")

    if health <= 0:
        print("die")
        game_over = True
    print(score)
def draw():
    screen.fill("black")
    spaceship.draw()
    for i in asteroids:
        i.draw()
    for i in projectiles:
        i.draw()
        
    screen.draw.text(f"score: {score}", topleft=(0,0), color="white", fontsize=70)
    screen.draw.text(f"health: {health}", topleft=(0,40), color="red", fontsize=70)
    if game_over:
        screen.draw.text("Game Over", center=(halfwidth, halfheight), color="red", fontsize=100)
        

pgzrun.go()