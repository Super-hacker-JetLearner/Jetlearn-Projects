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
score = 0
health = 10

window = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

space_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/space.png')
space_image = pygame.transform.scale(space_image, screen_size)

spaceship_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/spaceship2.png')

asteroid_image = pygame.image.load('/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/asteroid2.png')

big_asteroid = pygame.transform.scale_by(asteroid_image, 1.2)
medium_asteroid = pygame.transform.scale_by(big_asteroid, 0.6)
small_asteroid = pygame.transform.scale_by(medium_asteroid, 0.5)

font = pygame.font.SysFont('Times New Roman', 72)

# half_pi = math.pi/2
asteroid_appear_rate = (0.1,0.3)
last_asteroid = time.time()
time_to_asteroid = random.uniform(asteroid_appear_rate[0], asteroid_appear_rate[1])


class Projectile(pygame.sprite.Sprite):
    def __init__(self, position, direction, radius:int=5, color:tuple=(255,255,255), speed:int|float=10):
        pygame.sprite.Sprite.__init__(self)
        self.radius = radius
        self.rect = pygame.rect.Rect(position, (radius*2, radius*2))
        self.position = list(position)
        self.color = color
        direction += math.pi
        self.xv = math.cos(direction)*speed
        self.yv = math.sin(direction)*speed
    
    def update(self):
        self.position[0] += self.xv
        self.position[1] += self.yv
        self.rect.center = self.position
    def draw(self):
        pygame.draw.circle(window, self.color, self.position, self.radius)


    
    

projectile_group = pygame.sprite.Group()


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
        self.image = pygame.transform.rotate(self.original_image, math.degrees(-self.direction) + 90)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
    def make_projectile(self):
        if time.time() - self.last_shoot > self.shooting_speed:
            projectile_group.add(Projectile(self.position, direction=self.direction))
            self.last_shoot = time.time()


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, speed:int|float=0.7, size:int=None, position:tuple[int,int]|None=None, velocity:tuple|None=None):
        pygame.sprite.Sprite.__init__(self)
        if size is None:
            size = random.randint(0,2)
        if size == 0:
            self.image = small_asteroid
            self.size = 0
        elif size == 1:
            self.image = medium_asteroid
            self.size = 1
        elif size == 2:
            self.image = big_asteroid
            self.size = 2
            
        self.rect = self.image.get_rect()
        self.speed = speed
        
        # print(self.image.get_size())
        if position is None:
            position = [0,0]
            
            xy = random.choice(["x", "y"])
            if xy == "x":
                position[0] = random.choice([0, WIDTH])
                position[1] = random.randint(0,HEIGHT)
            else:
                position[1] = random.choice([0,HEIGHT])
                position[0] = random.randint(0,WIDTH)
        # self.rect = pygame.rect.Rect(position, self.image.get_size())
        self.rect.center = position
        direction_offset = random.uniform(-0.2, 0.2)
        self.position = list(position)
        if velocity is None:
            direction_to_spaceship = math.atan2(self.rect.centery-spaceship.rect.centery, self.rect.centerx-spaceship.rect.centerx)
            self.xv = math.cos(direction_to_spaceship+direction_offset + math.pi)*speed
            self.yv = math.sin(direction_to_spaceship+direction_offset + math.pi)*speed
        else:
            self.xv = velocity[0]
            self.yv = velocity[1]
        
    def update(self):
        # self.rect.x += self.xv
        # self.rect.y += self.yv
        self.position[0] += self.xv
        self.position[1] += self.yv
        
        self.rect.topleft = self.position
        # self.rect = pygame.rect.Rect(self.position, self.rect.size)
        
        # self.rect.move_ip(self.xv, self.yv)
    def draw(self):
        window.blit(self.image, self.position)
        # print(self.position, self.rect.center, self.rect.size)
        # print(self.rect)




spaceship = Spaceship((600,400))

asteroid_group = pygame.sprite.Group()
asteroid_group.add(Asteroid(0, 2))

# def check_collided(projectile, asteroid):
#     global score
#     if asteroid.rect.collidepoint(projectile.position):
#         score += 1
#         return True




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
    
    projectile_group.update()
    for i in projectile_group:
        i.draw()
        
        
    # window.blit(big_asteroid, (300,300))
    # window.blit(medium_asteroid, (500,500))
    # window.blit(small_asteroid, (700,700))
    if time.time() - last_asteroid > time_to_asteroid:
        asteroid_group.add(Asteroid())
        last_asteroid = time.time()
        time_to_asteroid = random.uniform(asteroid_appear_rate[0], asteroid_appear_rate[1])
    
    asteroid_group.update()
    # asteroid_group.draw(window)
    for i in asteroid_group:
        i.draw()
        
    collided_dictionary = pygame.sprite.groupcollide(projectile_group, asteroid_group, True, False)
    for projectile in collided_dictionary.keys():
        for asteroid in collided_dictionary[projectile]:
            score += 1
            if asteroid.size == 2:
                position = asteroid.position
                speed = asteroid.speed
                asteroid.kill()
                direction = math.atan2(projectile.position[1]-position[1], projectile.position[0]-position[0])
                for i in range (2):
                    random_direction = random.uniform(-90, 90)
                    total_direction = direction + random_direction
                    xv = math.cos(direction)*speed
                    yv = math.sin(direction)*speed
                    print(position)
                    new_asteroid = Asteroid(size=1, position=position, velocity=(xv,yv))
                    print(new_asteroid.position)
                    asteroid_group.add(new_asteroid)
                
            elif asteroid.size == 1:
                position = asteroid.position
                speed = asteroid.speed
                asteroid.kill()
                direction = math.atan2(projectile.position[1]-position[1], projectile.position[0]-position[0])
                for i in range (2):
                    random_direction = random.uniform(-90, 90)
                    total_direction = direction + random_direction
                    xv = math.cos(direction)*speed
                    yv = math.sin(direction)*speed
                    print(position)
                    new_asteroid = Asteroid(size=0, position=position, velocity=(xv,yv))
                    print(new_asteroid.position)
                    asteroid_group.add(new_asteroid)
            else:
                asteroid.kill()
            
            asteroid.rect = asteroid.image.get_rect()
    
    spaceship_collide_list = pygame.sprite.spritecollide(spaceship, asteroid_group, False)
    if len(spaceship_collide_list) > 0:
        health -= 1
        asteroid_group.empty()
    
    health_text = font.render(f'health: {health}', True, (255,0,0))
    score_text = font.render(f'score: {score}', True, (255,255,255))
    window.blit(health_text, (900,0))
    window.blit(score_text, (0,0))
            
    pygame.display.update()