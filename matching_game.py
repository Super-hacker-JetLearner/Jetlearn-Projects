import pygame
from pygame.locals import *

pygame.init()

WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

subway_surfer = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/subway surfer.png')
candy_crush = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/candy crush.jpg')
ludo = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/ludo.png')
temple_run = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/temple run.png')

game_logos = [subway_surfer, candy_crush, ludo, temple_run]
game_names = ['subway surfer', 'candy crush', 'ludo', 'temple run']

connecting = False
positions = []
lines = []

font = pygame.font.SysFont("Times New Roman", 40)

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    event = pygame.event.poll()
    if event.type == QUIT:
        pygame.quit()
        
    if event.type == MOUSEBUTTONDOWN:
        positions.append(pygame.mouse.get_pos())
        if connecting == False:
            connecting = True
        else:
            lines.append((positions[-2], positions[-1]))
            connecting = False
        
    
    
    window.fill((255,255,255))
    for i in range(4):
        window.blit(game_logos[i], (50, i*200))
        name = font.render(game_names[i], True, (0,0,0))
        window.blit(name, (550, i*200))
        
    for i in positions:
        pygame.draw.circle(window, (0,0,0), i, 30)
        
    for i in lines:
        pygame.draw.line(window, (0,0,0), i[0], i[1], width=10)
    
    pygame.display.update()
    