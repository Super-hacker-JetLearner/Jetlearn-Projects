import pygame
from pygame.locals import *
from random import *
import time



pygame.init()

WIDTH = 1200
HEIGHT = 800
screen_size = (WIDTH, HEIGHT)
window = pygame.display.set_mode(screen_size)

time_limit = 60


plastic_bag_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/plastic bag2.png')
plastic_bag_image = pygame.transform.scale(plastic_bag_image, (50,70))

paper_bag_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/paper bag2.png')
paper_bag_image = pygame.transform.scale(paper_bag_image, (50,70))

bin_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/bin.png')
bin_image = pygame.transform.scale(bin_image, (70,100))

pencil_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/pencil.png')
pencil_image = pygame.transform.scale(pencil_image, (50,70))

wood_box_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/wood box.png')
wood_box_image = pygame.transform.scale(wood_box_image, (50,70))

recycle_background_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/recycle background.png')
recycle_background_image = pygame.transform.scale(recycle_background_image, screen_size)

font = pygame.font.SysFont('Times New Roman', 100)
win_lose_font = pygame.font.SysFont('Times New Roman', 150)

class Bin(pygame.sprite.Sprite):
    def __init__(self, position:tuple, image:pygame.surface.Surface=bin_image, speed:int|float=10):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = position
        self.speed = speed
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if pressed_keys[K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if pressed_keys[K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if pressed_keys[K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
            
class Garbage(pygame.sprite.Sprite):
    def __init__(self, position:tuple, image:pygame.surface.Surface, non_recyclable:bool):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = position
        self.non_recyclable = non_recyclable
    def update(self):
        global score
        if self.rect.colliderect(bin.rect):
            if self.non_recyclable:
                score -= 5
                self.kill()
            else:
                score += 1
                self.kill()
                

garbage_group = pygame.sprite.Group()

def make_non_recyclable_garbage():
    for i in range (20):
        position = (randint(0,WIDTH), randint(0,HEIGHT))
        garbage = Garbage(position, image=plastic_bag_image, non_recyclable=True)
        garbage_group.add(garbage)
        

garbage_image_list = [paper_bag_image, wood_box_image, pencil_image]
def make_recyclable_garbage():
    for i in range (100):
        position = (randint(0,WIDTH), randint(0,HEIGHT))
        garbage = Garbage(position, image=choice(garbage_image_list), non_recyclable=False)
        garbage_group.add(garbage)
        
def make_garbage():
    make_non_recyclable_garbage()
    make_recyclable_garbage()
        
make_garbage()

bin = Bin((300,300))
score = 0


start_time = time.time()

clock = pygame.time.Clock()

game_state = 'running'

while True:
    clock.tick(60)
    window.blit(recycle_background_image, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    if game_state == 'running':
        bin.update()
        
        garbage_group.update()
        
        time_left = round(time_limit - (time.time() - start_time))
        print(time_left)
        if time_left <= 0:
            if score >= 50:
                game_state = 'win'
            else:
                game_state = 'lose'
            
    window.blit(bin.image, bin.rect)
    garbage_group.draw(window)
    
    score_text = font.render(f'{score}', True, (0,0,0))
    window.blit(score_text, (0,0))
    
    time_text = font.render(f'{time_left}', True, (0,0,0))
    window.blit(time_text, (1100,0))

    if game_state == 'win':
        win_text = win_lose_font.render('You Won!', True, (0,255,0))
        window.blit(win_text, (100,400))
    elif game_state == 'lose':
        lose_text = win_lose_font.render('You Lost!', True, (255,0,0))
        window.blit(lose_text, (100,400))

    pygame.display.update()