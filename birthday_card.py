import pygame
import time

pygame.init()


WIDTH = 800
HEIGHT = 800
refresh_rate = 2
pages = []

window = pygame.display.set_mode((WIDTH,HEIGHT))

font = pygame.font.SysFont("Times New Roman", 72)

image1 = pygame.image.load("/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/birthday card.jpg")
image1 = pygame.transform.scale(image1, (WIDTH,HEIGHT))




image2 = pygame.image.load("/Users/s932172@aics.espritscholen.nl/Desktop/game development/images/birthday card 2.jpg")
image2 = pygame.transform.scale(image2, (WIDTH,HEIGHT))

text1 = font.render("Happy Birthday", True, (0,0,0))
text2 = font.render("I hope you like the cake!!!", True, (0,0,0))

pages.append(((image1, (0,0)),(text1, (100,300))))
pages.append(((image2, (0,0)),(text2, (0,700))))
current_page = 0

clock = pygame.time.Clock()
the_time = time.time()

while True:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    
    window.fill((0,0,0))
    window.blit(pages[current_page][0][0], pages[current_page][0][1])
    window.blit(pages[current_page][1][0], pages[current_page][1][1])
    pygame.display.update()
    
    if round(time.time()) - round(the_time) > refresh_rate:
        the_time = time.time()
        current_page += 1
        if current_page == len(pages):
            current_page = 0
    
