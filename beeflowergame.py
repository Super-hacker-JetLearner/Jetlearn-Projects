import pgzrun


WIDTH = 300
HEIGHT = 250

bee = Actor("bee")
flower = Actor("flower")


# def on_key_down(key):
#     if key == 1073741906:
        
def update():
    if keyboard.left:
        bee.x -= 10
    elif keyboard.right:
        bee.x += 10
    elif keyboard.up:
        bee.y -= 10
    elif keyboard.down:
        bee.y += 10
        
    if bee.x > WIDTH:
        bee.x = WIDTH
    elif bee.x < 0:
        bee.x = 0
        
    if bee.y > HEIGHT:
        bee.y = HEIGHT
    elif bee.y < 0:
        bee.y = 0

def draw():
    screen.blit(("grass"), (0,0))
    bee.draw()


pgzrun.go()