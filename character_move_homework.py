import pygame
from pygame.locals import *


WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

mario = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/better mario.png')
# mario = pygame.transform.scale(mario, )
keys = [False, False, False, False]
class Mario():
    def __init__(self, image, position):
        self.image = image
        self.position = list(position)
    def draw(self):
        window.blit(self.image, self.position)

mario = Mario(mario, (500,500))

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    window.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                # mario.position[0] -= 10
                keys[0] = True
            if event.key == K_d:
                # mario.position[0] += 10
                keys[1] = True
            if event.key == K_w:
                # mario.position[1] -= 10
                keys[2] = True
            if event.key == K_s:
                # mario.position[1] += 10    
                keys[3] = True
                
        if event.type == KEYUP:
            if event.key == K_a:
                # mario.position[0] -= 10
                keys[0] = False
            if event.key == K_d:
                # mario.position[0] += 10
                keys[1] = False
            if event.key == K_w:
                # mario.position[1] -= 10
                keys[2] = False
            if event.key == K_s:
                # mario.position[1] += 10    
                keys[3] = False
    
    
        if keys[0]:
            mario.position[0] -= 10
        if keys[1]:
            mario.position[0] += 10
        if keys[2]:
            mario.position[1] -= 10
        if keys[3]:
            mario.position[1] += 10
            
    
    
    window.blit(mario.image, mario.position)
    
    pygame.display.update()