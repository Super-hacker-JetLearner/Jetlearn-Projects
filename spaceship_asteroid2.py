import pygame
from pygame.locals import *
import random
import math
import time

pygame.init()
pygame.mixer.init()

WIDTH = 1200
HEIGHT = 800
screen_size = (WIDTH, HEIGHT)
shooting_speed = 0.1

window = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

space_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/space.png')
space_image = pygame.transform.scale(space_image, screen_size)

spaceship_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/spaceship2.png')

asteroid_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/asteroid2.png')


class Projectile():
    def __init__(self, position, direction, radius:int=10, color:tuple=(255,255,255), speed:int|float=10):
        global projectiles
        projectiles.append(self)
        self.radius = radius
        self.position = list(position)
        self.color = color
        direction += math.pi
        self.xv = math.cos(direction)*speed
        self.yv = math.sin(direction)*speed
    
    def update(self):
        self.position[0] += self.xv
        self.position[1] += self.yv
        pygame.draw.circle(window, self.color, self.position, self.radius)
    def check_collision(self, position):
        difference_position = [self.position[0]-position[0], self.position[1]-self.position[1]]
        if math.sqrt(difference_position[0]**2 + difference_position[1]**2) < self.radius:
            return True
        else:
            return False
        

projectiles = []    


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, position, image:pygame.surface.Surface=spaceship_image, shooting_speed:float|int=shooting_speed):
        self.shooting_speed = shooting_speed
        self.last_shoot = time.time()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect()
        self.rect.center = position
        self.direction = 0
        self.position = position
    def change_direction(self):
        mouse_position = pygame.mouse.get_pos()
        difference_position = [self.rect.centerx-mouse_position[0], self.rect.centery-mouse_position[1]]
        self.direction = math.atan2(difference_position[1], difference_position[0])
        self.image = pygame.transform.rotate(self.original_image, -self.direction*180/math.pi + 90)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
    def make_projectile(self):
        if time.time() - self.last_shoot > self.shooting_speed:
            Projectile(self.position, direction=self.direction)
            self.last_shoot = time.time()


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image:pygame.surface.Surface=asteroid_image, speed:int|float=10):
        pygame.sprite.Sprite.__init__(self)
        size = random.randint(50,300)
        resized_image = pygame.transform.scale(image, (size,size))
        self.image = resized_image
        self.rect = self.image.get_rect()
        position = [random.randint(0,WIDTH), random.randint(0,HEIGHT)]
        self.rect.center = position
        direction = random.randint(0,math.pi*2)
        self.xv = math.cos(direction)*speed
        self.yv = math.sin(direction)*speed
        
    def update(self):
        self.rect.x += self.xv
        self.rect.y += self.yv


spaceship = Spaceship((600,400))


while True:
    clock.tick(60)
    window.blit(space_image, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEMOTION:
            spaceship.change_direction()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_SPACE]:
        spaceship.make_projectile()
            
    spaceship.update()
    window.blit(spaceship.image, spaceship.rect)
    
    for projectile in projectiles:
        projectile.update()
    
            
    pygame.display.update()