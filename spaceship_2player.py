import pygame
from pygame.locals import *
import time
import random

pygame.mixer.init()

pygame.init()

sound2 = pygame.mixer.Sound('/Users/s932172@aics.espritscholen.nl/Desktop/game development/sounds/Grenade+1.mp3')
sound1 = pygame.mixer.Sound('/Users/s932172@aics.espritscholen.nl/Desktop/game development/sounds/Gun+Silencer.mp3')
# print(sound1.get_volume())
# print(sound2.get_volume())
sound1.set_volume(0.5)
sound2.set_volume(0.5)

# bluehit = pygame.USEREVENT+1


WIDTH = 1200
HEIGHT = 800
spaceship_speed = 5
shooting_speed = 0.1
font = pygame.font.SysFont("Times New Roman", 72)

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('2 Player Spaceship Game')


space = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/space.jpg')
space = pygame.transform.scale(space, (WIDTH,HEIGHT))
red_spaceship = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/spaceship_red.png')
blue_spaceship = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/spaceship_blue.png')


red_spaceship = pygame.transform.scale_by(red_spaceship, 0.2)
# red_dimensions = (red_spaceship.get_width(), red_spaceship.get_height())
blue_spaceship = pygame.transform.scale_by(blue_spaceship, 0.2)
# blue_dimensions = (blue_spaceship.get_width(), blue_spaceship.get_height())

# blue_keys = [False, False, False, False]
# red_keys = [False, False, False, False]

# pygame.rect.RectType.

class Projectile():
    def __init__(self, position:tuple, direction:str="right", color:tuple=(255,255,0), dimensions:tuple=(20,10)):
        # self.position = list(position)
        global projectiles
        projectiles.append(self)
        self.color = color
        self.direction = direction
        # self.dimensions = dimensions
        self.rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
        self.rect.center = position
        
    def draw(self):
        # self.rect = pygame.Rect(self.position[0], self.position[1], self.dimensions[0], self.dimensions[1])
        pygame.draw.rect(window, self.color, self.rect)
        


class Spaceship():
    def __init__(self, image:pygame.surface.Surface, position:tuple, health:int = 10):
        self.image = image
        self.health = health
        self.last_shoot = time.time()
        # self.position = list(position)
        # self.dimensions = (image.get_width(), image.get_height())
        self.rect = image.get_rect()
        
        self.rect.center = list(position)
        
    def draw(self):
        window.blit(self.image, self.rect)


# pygame.event.post(pygame.event.Event(bluehit))


# red_rect = pygame.Rect(900,400, red_dimensions[0], red_dimensions[1])
# blue_rect = pygame.Rect(300,400, blue_dimensions[0], blue_dimensions[1])


red_spaceship = Spaceship(red_spaceship, (900,400))
blue_spaceship = Spaceship(blue_spaceship, (300,400))

line_dimensions = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)
# pygame.draw.rect(window, dimensions)

projectiles = []
# projectile = Projectile((500,500), "left")

clock = pygame.time.Clock()

red_health_position = (WIDTH-80, 20)
blue_health_position = (20,20)
winner = None

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         blue_keys[0] = True
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_a] and blue_spaceship.rect.x > 0:
        blue_spaceship.rect.x -= spaceship_speed
    if pressed_keys[K_d] and blue_spaceship.rect.x < 600-blue_spaceship.rect.width:
        blue_spaceship.rect.x += spaceship_speed
    if pressed_keys[K_w] and blue_spaceship.rect.y > 0:
        blue_spaceship.rect.y -= spaceship_speed
    if pressed_keys[K_s] and blue_spaceship.rect.y < HEIGHT-blue_spaceship.rect.height:
        blue_spaceship.rect.y += spaceship_speed
    if pressed_keys[K_SPACE]:
        if time.time() - blue_spaceship.last_shoot > shooting_speed:
            Projectile(blue_spaceship.rect.center, direction="right")
            blue_spaceship.last_shoot = time.time()
            
            sound1.play()
        
    if pressed_keys[K_LEFT] and red_spaceship.rect.x > 610:
        red_spaceship.rect.x -= spaceship_speed
    if pressed_keys[K_RIGHT] and red_spaceship.rect.x < WIDTH - red_spaceship.rect.width:
        red_spaceship.rect.x += spaceship_speed
    if pressed_keys[K_UP] and red_spaceship.rect.y > 0:
        red_spaceship.rect.y -= spaceship_speed
    if pressed_keys[K_DOWN] and red_spaceship.rect.y < HEIGHT-red_spaceship.rect.height:
        red_spaceship.rect.y += spaceship_speed
    if pressed_keys[K_RALT]: #or pressed_keys[K_RSUPER]:
        if time.time() - red_spaceship.last_shoot > shooting_speed:
            Projectile(red_spaceship.rect.center, direction="left")
            red_spaceship.last_shoot = time.time()
            
            sound1.play()
    
    for projectile in projectiles:
        if projectile.direction == "left":
            if blue_spaceship.rect.colliderect(projectile.rect):
                print("hit blue spaceship")
                blue_spaceship.health -= 1
                projectiles.remove(projectile)
                del projectile
                sound2.play()
        else:
            if red_spaceship.rect.colliderect(projectile.rect):
                red_spaceship.health -= 1
                projectiles.remove(projectile)
                del projectile
                sound2.play()
    
    for projectile in projectiles:
        if projectile.direction == "right":
            if projectile.rect.x < WIDTH:
                projectile.rect.x += 10
            else:
                projectiles.remove(projectile)
                del projectile
                continue
        if projectile.direction == "left":
            if projectile.rect.x > 0:
                projectile.rect.x -= 10
            else:
                projectiles.remove(projectile)
                del projectile
                continue


    # print(blue_spaceship.health, red_spaceship.health)
    if blue_spaceship.health == 0:
        winner = "red"
        break
    if red_spaceship.health == 0:
        winner = "blue"
        break
    # if blue_spaceship.position[0] < 0:
    #     blue_spaceship.position[0] = 0
    # if blue_spaceship.position[0]
    
    window.fill((0,0,0))
    window.blit(space, (0,0))
    if winner == "red":
        blue_spaceship.health = 0
    elif winner == "blue":
        red_spaceship.health = 0
    
    blue_health_text = font.render(f"{blue_spaceship.health}", True, "red")
    red_health_text = font.render(f"{red_spaceship.health}", True, "red")
    window.blit(blue_health_text, blue_health_position)
    window.blit(red_health_text, red_health_position)
    
    red_spaceship.draw()
    blue_spaceship.draw()
    pygame.draw.rect(window, (255,255,255),line_dimensions)
    for projectile in projectiles:  
        projectile.draw()
        
    if winner:
        winner_text = font.render(f"{winner} wins!", True, "green")
        window.blit(winner_text, (550, 400))
        
    
    

    
    pygame.display.update()
    
    
while True:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    window.fill((0,0,0))
    red_spaceship.draw()
    blue_spaceship.draw()
    winner_text = font.render(f"{winner} wins!", True, "green")
    window.blit(winner_text, (550, 400))
        
    
    

    
    pygame.display.update()