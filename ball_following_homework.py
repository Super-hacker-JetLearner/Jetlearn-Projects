import pygame
import random

screen_width = 800
screen_height = 800

half_screen_width = screen_width/2
half_screen_height = screen_height/2

window = pygame.display.set_mode((800,800))

clock = pygame.time.Clock()

class Ball():
    def __init__(self,position=(half_screen_width,half_screen_height), radius=10, color=(255,255,255), color_time=5):
        self.position = position
        self.radius = radius
        self.color = list(color)
        self.next_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.color_time = color_time
        self.color_time_left = color_time
        self.color_dif = ((self.color[0]-self.next_color[0])/(60*self.color_time), (self.color[1]-self.next_color[1])/(60*self.color_time), (self.color[2]-self.next_color[2])/(60*self.color_time))
        
    def move_ball(self):
        mouse_pos = pygame.mouse.get_pos()
        self.position = mouse_pos
        
    def draw_ball(self):
        pygame.draw.circle(window, color=self.color, center=self.position, radius=self.radius)
        
    def change_color(self):
        # for i in range (3):
        #     difference = self.color[i]-self.next_color[i]
        #     change = difference/(60*self.color_time)
        #     colors = [self.color[0], self.color[1], self.color[2]]
        #     colors[i] -= change
        #     self.color = (colors[0], colors[1], colors[2])
        # print(self.color)
        for i in range (3):
            self.color[i] -= self.color_dif[i]
        
        self.color_time_left -= 1/60
        if round(self.color_time_left) <= 0:
            self.next_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.color_time_left = self.color_time
            self.color_dif = ((self.color[0]-self.next_color[0])/(60*self.color_time), (self.color[1]-self.next_color[1])/(60*self.color_time), (self.color[2]-self.next_color[2])/(60*self.color_time))
            print(self.color_dif)
        
        print(self.color)
        print(self.next_color)
        print(self.color_time_left)
            

            


ball = Ball((half_screen_width,half_screen_height), 10, (255,255,0), 2)



while True:
    clock.tick(60)
    window.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.radius += 30
        
        if event.type == pygame.MOUSEBUTTONUP:
            ball.radius -= 10
        
    
            

            
    ball.move_ball()
    ball.draw_ball()
    ball.change_color()
            
    
            
    
    pygame.display.update()