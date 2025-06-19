import pgzrun
import random
import time

WIDTH = 1000
HEIGHT = 625
last_pressed = 0

satellites = []
positions = []
for i in range (8):
    satellite = Actor("satellite.png")
    satellite.x = random.randint(0,1000)
    satellite.y = random.randint(0,625)
    positions.append((satellite.x, satellite.y))
    satellites.append(satellite)


# def on_mouse_down(pos):
#     global last_pressed
#     for i in satellites:
#         if i.collidepoint(pos):
#             if satellites.index(i) == last_pressed:
#                 print("yeah")
#                 last_pressed = satellites.index(i)+1
#                 if satellites.index(i) != len(satellites)-1:
#                     positions[last_pressed].append( (satellites[satellites.index(i)].x, satellites[satellites.index(i)].y))
#                 else:
#                     pass

#             else:
#                 last_pressed = 0


# def draw():
#     screen.blit("space.jpg", (0,0))
#     for i in satellites:
#         i.draw()
#         screen.draw.text(f"{satellites.index(i)+1}", (i.x,i.y + 20))
        
#     # for i in range (last_pressed):
#     #     screen.draw.line((satellites[i].x, satellites[i].x), (satellites[i+1].x, satellites[i+1].x), "red")
#     for i in range(len(positions)-1):       
#         if positions[i+1] != (0,0):
#             screen.draw.line(positions[i], positions[i+1], "red")
the_time = time.time()
time_taken = 0 
stop = False    
           
            
            
def on_mouse_down(pos):
    global last_pressed
    for i in satellites:
        if i.collidepoint(pos):
            if satellites.index(i) == last_pressed:
                print("yeah")
                last_pressed += 1
            else:
                last_pressed = 0         




def update():
    global time_taken, stop
    if not stop:
        time_taken = round(time.time() - the_time, 2)
        if last_pressed == len(satellites):
            print("You have completed the game!")
            print(f"Time taken: {time_taken} seconds")
            stop = True
            screen.draw.text(f"You have completed the game in {time_taken} seconds!", (WIDTH//2 - 200, HEIGHT//2), color="white", fontsize=40)


def draw():
    if not stop:
        screen.blit("space.jpg", (0,0))
        for i in satellites:
            i.draw()
            screen.draw.text(f"{satellites.index(i)+1}", (i.x,i.y + 20))

        for i in range(last_pressed-1):
            screen.draw.line(positions[i], positions[i+1], "red")

        screen.draw.text(f"Time: {time_taken} seconds", (10, 10), color="white", fontsize=30)

pgzrun.go()