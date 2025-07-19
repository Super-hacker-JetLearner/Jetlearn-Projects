import pygame

window = pygame.display.set_mode( (800,800) )
clock = pygame.time.Clock()


class the_rect():


    # color = "white"
    # width = 1
    
    def __init__(self):
        print("initializing")
    
    
    def rect(self, position, size, color="white", width=1):
        # global my_rect
        self.my_rect =  pygame.Rect(position, size,)
        self.the_color = color
        self.the_width = width
    
    def draw(self):
        pygame.draw.rect(window, rect=self.my_rect, width=self.the_width, color=self.the_color)
        
        
        
rect1 = the_rect()
rect1.rect((40,40), (50,50), color="red", width=20)

rect2 = the_rect()
rect2.rect((80,80), (50,50), color="red", width=20)
# rect1 = the_rect().rect((40,40), (50,50))
# rect1 = the_rect().rect((40,40), (50,50))

# the_rect().draw(color="red", width=20)



while True:
    clock.tick(60)
    # window.fill(0,0,0)
    window.fill("black")
    # the_rect().draw()
    rect1.draw()
    rect2.draw()

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    
    pygame.display.update()