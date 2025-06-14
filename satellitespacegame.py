import pgzrun
import random

WIDTH = 1000
HEIGHT = 625
last_pressed = 0

satellites = []
positions = []
for i in range (8):
    satellite = Actor("satellite.png")
    satellite.x = random.randint(0,1000)
    satellite.y = random.randint(0,625)
    positions.append((0,0))
    satellites.append(satellite)


def on_mouse_down(pos):
    global last_pressed
    for i in satellites:
        if i.collidepoint(pos):
            if satellites.index(i) == last_pressed:
                print("yeah")
                last_pressed = satellites.index(i)+1
                if satellites.index(i) != len(satellites)-1:
                    positions[last_pressed].append( (satellites[satellites.index(i)].x, satellites[satellites.index(i)].y))
                else:
                    
                    
                
            else:
                last_pressed = 0

def draw():
    screen.blit("space.jpg", (0,0))
    for i in satellites:
        i.draw()
        screen.draw.text(f"{satellites.index(i)+1}", (i.x,i.y + 20))
        
    # for i in range (last_pressed):
    #     screen.draw.line((satellites[i].x, satellites[i].x), (satellites[i+1].x, satellites[i+1].x), "red")
    for i in range(len(positions)-1):       
        if positions[i+1] != (0,0):
            screen.draw.line(positions[i], positions[i+1], "red")
            

pgzrun.go()