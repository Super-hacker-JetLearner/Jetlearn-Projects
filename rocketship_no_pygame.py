import pygame
from pygame.locals import *
import time

pygame.init()

WIDTH = 800
HEIGHT = 800

HALF_WIDTH = WIDTH/2
HALF_HEIGHT = HEIGHT/2

window = pygame.display.set_mode((WIDTH,HEIGHT))

space = pygame.image.load("/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/space.jpg")
space = pygame.transform.scale(space, (WIDTH,HEIGHT))
spaceship = pygame.image.load("/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/spaceship.png")
spaceship_image = pygame.transform.scale(spaceship, (100,100))


keys = [False, False, False, False]

class Spaceship():
    def __init__(self, image):
        self.position = [HALF_WIDTH, HALF_HEIGHT]
        self.image = image
        
        
spaceship = Spaceship(spaceship_image)

clock = pygame.time.Clock()


while True:
    clock.tick(60)
    window.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                # spaceship.position[0] -= 10
                keys[0] = True
            if event.key == K_d:
                # spaceship.position[0] += 10
                keys[1] = True
            if event.key == K_w:
                # spaceship.position[1] -= 10
                keys[2] = True
            if event.key == K_s:
                # spaceship.position[1] += 10    
                keys[3] = True
                
        if event.type == KEYUP:
            if event.key == K_a:
                # spaceship.position[0] -= 10
                keys[0] = False
            if event.key == K_d:
                # spaceship.position[0] += 10
                keys[1] = False
            if event.key == K_w:
                # spaceship.position[1] -= 10
                keys[2] = False
            if event.key == K_s:
                # spaceship.position[1] += 10    
                keys[3] = False
    
    
        if keys[0]:
            spaceship.position[0] -= 10
        if keys[1]:
            spaceship.position[0] += 10
        if keys[2]:
            spaceship.position[1] -= 10
        if keys[3]:
            spaceship.position[1] += 10
            
    if  not all(keys):
        spaceship.position[1] += 2
    
    window.blit(spaceship.image, spaceship.position)
    
    pygame.display.update()