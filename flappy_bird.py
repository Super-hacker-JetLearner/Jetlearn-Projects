import pygame
from pygame.locals import *
import random
import time

pygame.init()

WIDTH = 1200
HEIGHT = 800
screen_size = (WIDTH, HEIGHT)
half_width = WIDTH/2
half_height = HEIGHT/2

window = pygame.display.set_mode(screen_size)
score = 0
high_score = 0


background = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/flappy bird background.png')
background = pygame.transform.scale(background, screen_size)

ground = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/flappy bird ground.png')
ground = pygame.transform.scale(ground, (WIDTH, 100))

ground2 = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/flappy bird ground.png')
ground2 = pygame.transform.scale(ground, (WIDTH, 100))

pipe_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/flappy bird pipe.png')
pipe_image = pygame.transform.scale(pipe_image, (100,HEIGHT))

restart_button_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/flappy bird restart button.png')
# restart_button_image = pygame.transform.scale_by(restart_button_image, 1)

font = pygame.font.SysFont('Times New Roman', 72)


rect1 = ground.get_rect()
rect1.topleft = (0,700)

rect2 = ground2.get_rect()
rect2.topleft = (800,700)

ground_speed = 5
gravity = 0.2
jump_speed = 1.5
maximum_up_speed = 7
pipe_appear_rate = (2,3)
time_to_pipe = random.uniform(pipe_appear_rate[0], pipe_appear_rate[1])
last_pipe_time = time.time()
# last_clicked = False

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
        self.image = self.images[self.current_image]
        self.rect = self.rects[self.current_image]
    
    def update(self):
        self.yv += gravity
        self.position[1] += self.yv
        for rect in self.rects:
            rect.center = self.position
        
        if time.time() - self.the_time > self.image_change_speed:
            self.the_time = time.time()
            self.current_image += 1
            if self.current_image == 3:
                self.current_image = 0
            self.image = self.images[self.current_image]
            self.rect = self.rects[self.current_image]
            
            
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.yv -= jump_speed
        if self.yv < -maximum_up_speed:
            self.yv = -maximum_up_speed
            
            
        


        


class Pipe(pygame.sprite.Sprite):
    def __init__(self, height_position, gap_size=200, top_bottom:int=1, move_speed=10):
        this_pipe = pipe_image
        self.move_speed = move_speed
        pygame.sprite.Sprite.__init__(self)
        self.top_bottom = top_bottom
        if top_bottom == 1:
            this_pipe = pygame.transform.flip(this_pipe, False, True)
            self.image = this_pipe
            self.rect = this_pipe.get_rect()
            self.rect.bottomleft = (WIDTH, height_position - gap_size/2)
            self.is_done = False
        else:
            self.image = this_pipe
            self.rect = this_pipe.get_rect()
            self.rect.topleft = (WIDTH, height_position + gap_size/2)
        
        
    def update(self):
        global score
        self.rect.x -= self.move_speed
        if self.rect.right < 0:
            self.kill()
        if self.top_bottom == 1:
            if not self.is_done:
                if self.rect.centerx < bird_group.sprites()[0].rect.centerx:
                    score += 1
                    self.is_done = True
            
            
class Restart_Button(pygame.sprite.Sprite):
    def __init__(self, position:tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = restart_button_image
        self.rect = restart_button_image.get_rect()
        self.rect.center = position
    def update(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            global time_to_pipe, last_pipe_time, score, game_over, game_start
            bird_group.empty()
            bird_group.add(Bird(100,400))
            pipe_group.empty()
            last_pipe_time = time.time()
            time_to_pipe = random.uniform(pipe_appear_rate[0], pipe_appear_rate[1])
            score = 0
            game_over = False
            game_start = False
            self.kill()
            
        

pipe_group = pygame.sprite.Group()

restart_button_group = pygame.sprite.Group()

top_limit = 100
bottom_limit = HEIGHT-100

def make_pipe():
    height_position = random.randint(top_limit, bottom_limit)
    pipe_group.add(Pipe(height_position, top_bottom=1))
    pipe_group.add(Pipe(height_position, top_bottom=0))



bird_group = pygame.sprite.Group()
bird_group.add(Bird(100,400))


game_start = False

clock = pygame.time.Clock()

game_over = False

high_score_x = half_width - 100

while True:
    dt = clock.tick(60)
    window.fill((0,0,0))
    # last_clicked = False
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == MOUSEBUTTONDOWN and not game_over:
            game_start = True
        

   
   
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
        
        
    
    # bird_group.animate()
        bird_group.update()
    
        if time.time() - last_pipe_time > time_to_pipe:
            time_to_pipe = random.uniform(pipe_appear_rate[0], pipe_appear_rate[1])
            last_pipe_time = time.time()
            make_pipe()
    
        pipe_group.update()
    
        if pygame.sprite.groupcollide(bird_group, pipe_group, dokilla=False, dokillb=False):
            if not game_over:
                print('dead')
                game_over = True
                game_start = False
                restart_button_group.add(Restart_Button((half_width, half_height)))
                if score > high_score:
                    high_score = score


    bird_group.draw(window)
    pipe_group.draw(window)
    
    score_text = font.render(f'{score}', True, (0,0,0))
    window.blit(score_text, (half_width,0))

   
    restart_button_group.update()
    restart_button_group.draw(window)
    
    if game_over:
        high_score_text = font.render(f'high score: {high_score}', True, (0,0,0))
        window.blit(high_score_text, (high_score_x, 200))
            
    pygame.display.update()