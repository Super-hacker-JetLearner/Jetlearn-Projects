import pgzrun
import random


WIDTH = 300
HEIGHT = 250

bee = Actor("bee")
flower = Actor("flower")
score = 0

speed = 5

# def on_key_down(key):
#     if key == 1073741906:

flower.x = random.randint(0,300)
flower.y = random.randint(0,250)

def update():
    global score, speed
    if keyboard.left:
        bee.x -= speed
    elif keyboard.right:
        bee.x += speed
    elif keyboard.up:
        bee.y -= speed
    elif keyboard.down:
        bee.y += speed
        
    if bee.x > WIDTH:
        bee.x = WIDTH
    elif bee.x < 0:
        bee.x = 0
        
    if bee.y > HEIGHT:
        bee.y = HEIGHT
    elif bee.y < 0:
        bee.y = 0
        

        

def draw():
    global score
    if bee.colliderect(flower):
        score += 1
        print(score)
        flower.x = random.randint(0,300)
        flower.y = random.randint(0,250)
    
    screen.blit(("grass"), (0,0))
    bee.draw()
    flower.draw()

    screen.draw.text(f"score: {score}", (150,10))

pgzrun.go()