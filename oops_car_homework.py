import pygame
from pygame.locals import *
import time
from random import randint, uniform

pygame.init()

WIDTH = 800
HEIGHT = 800
screen_size = (WIDTH, HEIGHT)
window = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

apple_appear_rate = (0.5, 2)
disappear_time = (0.5,2)

apples = []

class Car():
    def __init__(self, position:tuple, color=(0,0,255), disappear_time=5):
        self.rect = pygame.rect.Rect(position, (50,50))
        self.color = color
        self.score = 0
        self.speed = 10
    def check_apple(self, apples):
        for apple in apples:
            if self.rect.colliderect(apple.rect):
                self.score += 1
                apples.remove(apple)
                del apple
    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        
class Apple():
    def __init__(self, boundaries:tuple=screen_size, disappear_time=uniform(disappear_time[0], disappear_time[1])):
        self.rect = pygame.rect.Rect((randint(0,boundaries[0]), randint(0,boundaries[1])), (20,20))
        global apples
        apples.append(self)
        self.disappear_time = disappear_time
        self.color = (255,0,0)
        self.time = time.time()
    def check_time(self):
        time_left = time.time() - self.time
        if time_left > self.disappear_time:
            apples.remove(self)
            del self      
    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)


car = Car((500,500))

last_apple_time = time.time()
time_to_apple = uniform(apple_appear_rate[0], apple_appear_rate[1])

font = pygame.font.SysFont('Times New Roman', 72)

while True:
    clock.tick(60)
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_a] and car.rect.left > 0:
        car.rect.x -= car.speed
    if pressed_keys[K_d] and car.rect.right < WIDTH:
        car.rect.x += car.speed
    if pressed_keys[K_w] and car.rect.top > 0:
        car.rect.y -= car.speed
    if pressed_keys[K_s] and car.rect.bottom < HEIGHT:
        car.rect.y += car.speed
        
    if time.time() - last_apple_time > time_to_apple:
        last_apple_time = time.time()
        time_to_apple = uniform(apple_appear_rate[0], apple_appear_rate[1])
        Apple()
    
    for apple in apples:
        apple.check_time()
        apple.draw()
    
    car.check_apple(apples)
    car.draw()
    print(car.score)
    
    score_text = font.render(f'{car.score}', True, (255,255,255))
    window.blit(score_text, (0,0))
    
            
    pygame.display.update()