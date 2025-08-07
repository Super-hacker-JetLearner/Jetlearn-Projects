import pygame
from pygame.locals import *
import time
import random

pygame.init()
pygame.mixer.init()


sound2 = pygame.mixer.Sound('/Users/s932172@aics.espritscholen.nl/Desktop/game development/sounds/Grenade+1.mp3')
sound1 = pygame.mixer.Sound('/Users/s932172@aics.espritscholen.nl/Desktop/game development/sounds/Gun+Silencer.mp3')
sound3 = pygame.mixer.Sound('/Users/s932172@aics.espritscholen.nl/Desktop/game development/sounds/explosion.mp3')
# print(sound1.get_volume())
# print(sound2.get_volume())
sound1.set_volume(0.1)
sound2.set_volume(0.1)
sound3.set_volume(0.1)

enemy_spaceship_appear_rate = (1,2)
next_enemy_time = random.uniform(enemy_spaceship_appear_rate[0], enemy_spaceship_appear_rate[1])
last_enemy_time = time.time()
score = 0
font = pygame.font.SysFont('Times New Roman', 72)

WIDTH = 1200
HEIGHT = 800

window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

space_speed = 5
space_list = []
for i in range (2):
    space = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/space.jpg')
    space = pygame.transform.scale(space, (WIDTH, HEIGHT))
    space_rect = space.get_rect()
    space_list.append((space, space_rect))

space_list[0][1].topleft = (0,0)
space_list[1][1].topleft = (WIDTH,0)



spaceship = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/spaceship_blue.png')
spaceship = pygame.transform.scale_by(spaceship, 0.2)

enemy_spaceship_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/spaceship_red.png')
enemy_spaceship_image = pygame.transform.scale_by(enemy_spaceship_image, 0.2)

projectiles = []
class Projectile():
    def __init__(self, position:tuple, direction:str="right", dimensions:tuple=(20,10), color:tuple=(255,255,0), speed:int=10):
        global projectiles
        projectiles.append(self)
        self.rect = pygame.Rect(position, dimensions)
        self.color = color
        if direction == "right":
            self.direction = 1
        else:
            self.direction = -1
        
        self.speed = speed
        
    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        
        
    def move(self):
        global projectiles
        # if self.direction == "right":
        #     if self.rect.x < WIDTH:
        #         self.rect.x += self.speed
        #     else:
        #         projectiles.remove(self)
        #         del self
        # else:
        #     if self.rect.x > 0:
        #         self.rect.x -= self.speed
        #     else:
        #         projectiles.remove(self)
        #         del self
        self.rect.x += self.direction * self.speed
        if self.rect.x > WIDTH or self.rect.x < 0:
            projectiles.remove(self)
            del self
    
enemy_spaceships = []
class Enemy_Spaceship():
    global enemy_spaceships
    def __init__(self, image:pygame.surface.Surface, position:tuple, health:int=3, movement_speed:int=5):
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = position
        self.health = health
        self.movement_speed = movement_speed
        enemy_spaceships.append(self)
        
    def draw(self):
        window.blit(self.image, self.rect)
    
    def move(self):
        self.rect.x -= self.movement_speed
        if self.rect.right < 0:
            enemy_spaceships.remove(self)
            del self
            

class Spaceship():
    def __init__(self, image:pygame.surface.Surface, position:tuple, health:int=10, movement_speed:int = 5, shooting_speed:float = 0.2):
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = position
        self.health = health
        self.shooting_speed = shooting_speed
        self.movement_speed = movement_speed
        self.last_shoot = time.time()
    def draw(self):
        window.blit(self.image, self.rect)
    def shoot(self):
        if time.time() - self.last_shoot > self.shooting_speed:
            Projectile(self.rect.center, direction="right")
            sound1.play()
            self.last_shoot = time.time()
    def move(self, direction:str="right"):
        if direction == "left" and spaceship.rect.left > 0:
            spaceship.rect.x -= spaceship.movement_speed
        if direction == "right" and spaceship.rect.right < WIDTH:
            spaceship.rect.x += spaceship.movement_speed
        if direction == "up" and spaceship.rect.top > 0:
            spaceship.rect.y -= spaceship.movement_speed
        if direction == "down" and spaceship.rect.bottom < HEIGHT:
            spaceship.rect.y += spaceship.movement_speed
        
        
spaceship = Spaceship(spaceship, (500,500))
enemy_spaceship = Enemy_Spaceship(enemy_spaceship_image, (WIDTH,500))

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_a]:
        spaceship.move("left")
    if pressed_keys[K_d]:
        spaceship.move("right")
    if pressed_keys[K_w]:
        spaceship.move("up")
    if pressed_keys[K_s]:
        spaceship.move("down")
    if pressed_keys[K_SPACE]:
        spaceship.shoot()
    
    
    window.fill((0,0,0))
    for space in space_list:
        window.blit(space[0], space[1])
        space[1].x -= space_speed
        if space[1].left <= -WIDTH:
            space[1].left = WIDTH
    spaceship.draw()
    for i in enemy_spaceships:
        i.move()
        i.draw()
    
    for i in projectiles:
        i.move()
        i.draw()
        
    for i in projectiles:
        for j in enemy_spaceships:
            if i.rect.colliderect(j.rect):    
                score += 100
                sound2.play()
                projectiles.remove(i)
                enemy_spaceships.remove(j)
                del i
                del j
                break
            
    for i in enemy_spaceships:
        if spaceship.rect.colliderect(i.rect):
            spaceship.health -= 1
            sound3.play()
            enemy_spaceships.remove(i)
            del i
            
    
    print(score)
    print(spaceship.health)
    health_text = font.render(f'health: {spaceship.health}', True, (255,0,0))
    score_text = font.render(f'score: {score}', True, (255,255,255))
    window.blit(health_text, (900,0))
    window.blit(score_text, (0,0))
    
    if time.time() - last_enemy_time > next_enemy_time:
        last_enemy_time = time.time()
        next_enemy_time = random.uniform(enemy_spaceship_appear_rate[0], enemy_spaceship_appear_rate[1])
        enemy_spaceship = Enemy_Spaceship(enemy_spaceship_image, (WIDTH, random.randint(0,HEIGHT)))
    
    
    
    pygame.display.update()