import pgzrun

WIDTH = 1200
HEIGHT = 800
spaceship = Actor("spaceship.png")
spaceship.center = WIDTH/2, HEIGHT -50

# def on_key_down(key):
#     if key == keys.LEFT:
#         spaceship.x -= 10
#     if key == keys.RIGHT:
#         spaceship.x += 10
projectiles = []
def make_projectile(position):
    global projectile
    projectile = Actor()

def update():
    if keyboard.left:
        spaceship.x -= 10
    if keyboard.right:
        spaceship.x += 10
    if keyboard.up:
        
        
        
    if spaceship.x < 0:
        spaceship.x = 0
    if spaceship.x > WIDTH:
        spaceship.x = WIDTH

def draw():
    screen.fill("black")
    spaceship.draw()


pgzrun.go()