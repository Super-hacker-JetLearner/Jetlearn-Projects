import pgzrun
import time
import random

WIDTH = 1200
HEIGHT = 800
spaceship = Actor("spaceship.png")
spaceship.center = WIDTH/2, HEIGHT -50
shoot_speed = 0.1
projectile_speed = 10
side_speed = 7
down_speed = 50
score = 0
win_points = 6000

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
directions = []
# def make_bug():
#     bug = Actor("bug.png")
#     bug.center = random.randint(0,WIDTH),0
#     bugs.append(bug)
start_time = time.time()
game_length = 30

def make_bugs():
    global bugs, directions
    current_bugs = []
    the_bug = Actor("bug.png")
    the_bug.center = random.randint(0,WIDTH-281), 0
    current_bugs.append(the_bug)
    for i in range (4):
        bug = Actor("bug.png")
        bug.center = the_bug.x+(i*70), 0
        current_bugs.append(bug)
    bugs.append(current_bugs)
    directions.append("right")
health = 3
game_over = False
game_won = False

def update():
    global last_shot, the_time, bug_time, score, health, game_over, directions, game_won
    if game_over or game_won:
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
        make_bugs()
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
            
    # for i in bugs:
    #     for j in i:
    #     i.y += side_speed
    #     # i.draw()
    #     if i.y > HEIGHT:
    #         try:
    #             bugs.remove(i)
    #         except:
    #             pass
    for i in bugs:
        try:
            if i[0].x < 0:
                directions[bugs.index(i)] = "right"
                for j in i:
                    j.y += down_speed
            if i[-1].x > WIDTH:
                directions[bugs.index(i)] = "left"
                for j in i:
                    j.y += down_speed
        except:
            pass
        try:
            for j in i:
                if directions[bugs.index(i)] == "left":
                    j.x -= side_speed
                else:
                    j.x += side_speed
        except:
            pass
    
    
    
    
    
    for i in projectiles:
        for j in bugs:
            for b in j:
                try:
                    if i.colliderect(b):
                        projectiles.remove(i)
                        j.remove(b)
                        # del i
                        # del j
                        score += 100
                except:
                    pass
                
    for i in bugs:
        for b in i:
            if spaceship.colliderect(b):
                health -= 1
                i.remove(b)
            # print(health)
    # print(score)
    if health <= 0:
        # print("game over")
        game_over = True
        
    if time.time() - start_time > game_length:
        if score > win_points:
            game_won = True
        else:
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
        for b in i:
            b.draw()
            # del i
    screen.draw.text(str(score), topleft = (50,10), color="white", fontsize=60)
    screen.draw.text(str(health), topleft = (10, 10), color="red", fontsize=60)
    if not game_won:
        screen.draw.text(str(round(game_length-(time.time()-start_time))), topright=(WIDTH-10,10), color="white", fontsize=60)
    else:
        screen.draw.text("0", topright=(WIDTH-10,10), color="white", fontsize=60)
    
    if game_over:
        screen.draw.text("Game Over", center=(half_width, half_height), color="red", fontsize=150)
    
    if game_won:
        screen.draw.text("You Won!", center=(half_width, half_height), color="green", fontsize=150)

pgzrun.go()