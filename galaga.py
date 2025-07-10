import pgzrun
import time
import random

WIDTH = 1200
HEIGHT = 800
spaceship = Actor("spaceship.png")
spaceship.center = WIDTH/2, HEIGHT -50
shoot_speed = 0.1
projectile_speed = 10
bug_speed = 7
score = 0

# def on_key_down(key):
#     if key == keys.LEFT:
#         spaceship.x -= 10
#     if key == keys.RIGHT:
#         spaceship.x += 10
the_time = time.time()
bug_time = random.uniform(1,3)


last_shot = 0
projectiles = []
def make_projectile(position):
    global projectile
    projectile = Actor("bullet.png")
    projectile.center = position
    projectiles.append(projectile)

bugs = []
def make_bug():
    bug = Actor("bug.png")
    bug.center = random.randint(0,WIDTH),0
    bugs.append(bug)
health = 3
game_over = False
def update():
    global last_shot, the_time, bug_time, score, health, game_over
    if game_over:
        return
    if keyboard.left:
        spaceship.x -= 10
    if keyboard.right:
        spaceship.x += 10
    if keyboard.up:
        if time.time() - last_shot > shoot_speed:
            make_projectile(spaceship.midtop)
            last_shot = time.time()
        
    if time.time() - the_time > bug_time:
        make_bug()
        the_time = time.time()
        bug_time = random.uniform(1,3)    
    if spaceship.x < 0:
        spaceship.x = 0
    if spaceship.x > WIDTH:
        spaceship.x = WIDTH

    
    for i in projectiles:
        i.y -= projectile_speed
        # i.draw()
        if i.y < 0:
            try:
                projectiles.remove(i)
            except:
                pass
            # del i
            
    for i in bugs:
        i.y += bug_speed
        # i.draw()
        if i.y > HEIGHT:
            try:
                bugs.remove(i)
            except:
                pass
    
    
    
    
    
    
    for i in projectiles:
        for j in bugs:
            try:
                if i.colliderect(j):
                    projectiles.remove(i)
                    bugs.remove(j)
                    # del i
                    # del j
                    score += 100
            except:
                pass
                
    for i in bugs:
        if spaceship.colliderect(i):
            health -= 1
            bugs.remove(i)
            # print(health)
    # print(score)
    if health <= 0:
        # print("game over")
        game_over = True
        
half_width = WIDTH/2
half_height = HEIGHT/2
def draw():
    screen.fill("black")
    spaceship.draw()
    for i in projectiles:
        i.draw()
            # del i
    for i in bugs:
        i.draw()
            # del i
    screen.draw.text(str(score), topleft = (50,10), color="white", fontsize=60)
    screen.draw.text(str(health), topleft = (10, 10), color="red", fontsize=60)
    if game_over:
        screen.draw.text("Game Over", center=(half_width, half_height), color="red", fontsize=150)

pgzrun.go()