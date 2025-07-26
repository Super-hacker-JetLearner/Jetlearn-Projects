import pygame
from pygame.locals import *



WIDTH = 800
HEIGHT = 800

window = pygame.display.set_mode((WIDTH, HEIGHT))

light_bulb_on = pygame.image.load("/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/light_bulb_on.png")
light_bulb_off = pygame.image.load("/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/light_bulb_off.png")
light_bulb_on = pygame.transform.scale(light_bulb_on, (100,169))
light_bulb_off = pygame.transform.scale(light_bulb_off, (100,169))
light_bulbs = [light_bulb_off, light_bulb_on]

clock = pygame.time.Clock()
the_time = pygame.time.get_ticks()
change_rate = 2
change_rate *= 1000
current_light_bulb = 0

while True:
    clock.tick(60)
    window.fill((0,0,0))
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    window.blit(light_bulbs[current_light_bulb], (200,200))
    print(current_light_bulb)
    print(pygame.time.get_ticks())
    if pygame.time.get_ticks() - the_time > change_rate:
        the_time = pygame.time.get_ticks()
        current_light_bulb += 1
        if current_light_bulb == len(light_bulbs):
            current_light_bulb = 0
    
    pygame.display.update()