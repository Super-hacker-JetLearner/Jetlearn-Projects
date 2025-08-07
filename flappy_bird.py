import pygame
from pygame.locals import *
import random
import time

pygame.init()

WIDTH = 1200
HEIGHT = 800
screen_size = (WIDTH, HEIGHT)
window = pygame.display.set_mode(screen_size)


background = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/flappy bird background.png')
background = pygame.transform.scale(background, screen_size)

ground = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/flappy bird ground.png')
ground = pygame.transform.scale(ground, (WIDTH, 100))

ground2 = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/flappy bird ground.png')
ground2 = pygame.transform.scale(ground, (WIDTH, 100))

rect1 = ground.get_rect()
rect1.topleft = (0,700)

rect2 = ground2.get_rect()
rect2.topleft = (800,700)

ground_speed = 5
gravity = 0.2
up_speed = 10


class Bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image_change_speed = 0.1
        self.images = []
        self.rects = []
        self.position = [x,y]
        self.yv = 0
        self.the_time = time.time()
        for i in range (3):
            flappy = pygame.image.load(f'/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/flappy bird {i+1}.png')
            # flappy = pygame.transform.scaleby(flappy, 1)
            self.images.append(flappy)
            flappy_rect = flappy.get_rect()
            flappy_rect.center = self.position
            self.rects.append(flappy_rect)
            
        self.current_image = 0
    
    def move(self):
        self.yv += gravity
        self.position[1] += self.yv
        
    def draw(self):
        window.blit(self.images[self.current_image], self.position)
    def animate(self):
        if time.time() - self.the_time > flappy_bird.image_change_speed:
            self.the_time = time.time()
            flappy_bird.current_image += 1
            if flappy_bird.current_image == 3:
                flappy_bird.current_image = 0
                
                
class Pipe():
    def __init__(self, height)




flappy_bird = Bird(100,400)

game_start = False

clock = pygame.time.Clock()
while True:
    dt = clock.tick(60)
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == MOUSEBUTTONDOWN:
            game_start = True
            
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_SPACE]:
        flappy_bird.position[1] -= up_speed
        flappy_bird.yv = 0
    window.blit(background, (0,0))
    window.blit(ground, rect1)
    window.blit(ground2,rect2)
    if game_start:
        rect1.x -= ground_speed
        rect2.x -= ground_speed
        if rect1.left <= -800:
            rect1.left = 800
        if rect2.left <= -800:
            rect2.left = 800
        
        flappy_bird.move()
        
    
    flappy_bird.animate()
    flappy_bird.draw()

            
    pygame.display.update()