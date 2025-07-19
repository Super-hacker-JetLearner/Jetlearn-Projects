import pgzrun
import random
import math

TITLE = "bouncy ball"
HEIGHT = 800
WIDTH = 800
GRAVITY = 2000

class Ball():
    def __init__(self, position, color):
        print("making ball")
        self.y = position[0]
        self.x = position[1]
        self.color = color
        
        self.xv = random.randint(-1000,1000)
        self.yv = random.randint(-1000, 1000)
        self.radius = 20
        
    def draw(self):
        screen.draw.filled_circle((self.x,self.y), self.radius, self.color)
        

balls = []

colors = ["red", "green", "blue", "orange", "yellow", "purple"]
for i in range(10):
    ball = Ball((random.randint(50,750),random.randint(50,750)), random.choice(colors))
    balls.append(ball)

# def on_key_down(key):
#     if key == keys.UP:
#         ball.yv = -200
double_radius = ball.radius * 2

def update(dt):
    
    if keyboard.up:
        for ball in balls:
            ball.yv -= 50
    
    
    for ball in balls:
        prev_yv = ball.yv
        ball.yv = ball.yv + GRAVITY*dt
        ball.y += (ball.yv+prev_yv)*0.5*dt
        
        if ball.y + ball.radius > HEIGHT:
            ball.y = HEIGHT-ball.radius
            ball.yv *= -1
            ball.yv *= 0.9
            
            

        ball.x += ball.xv * dt

        
        if ball.x + ball.radius > WIDTH:
            ball.x = WIDTH - ball.radius
            ball.xv *= -1
            ball.xv *= 0.9
            
        if ball.x - ball.radius < 0:
            ball.x = 0 + ball.radius
            ball.xv *= -1
            ball.xv *= 0.9
        
        
        
        for i in balls:
            try:
                if i != ball:
                    x_dif = ball.x - i.x
                    y_dif = ball.y - i.y
                    if math.sqrt(x_dif*x_dif + y_dif*y_dif) > double_radius:
                        ball.xv *= -1
                        ball.yv *= -1
                        i.yv *= -1
                        i.xv *= -1
            except:
                pass



def draw():
    screen.fill("black")
    for ball in balls:
        ball.draw()
    
    
pgzrun.go()