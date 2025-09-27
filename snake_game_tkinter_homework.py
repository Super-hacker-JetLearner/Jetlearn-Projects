from tkinter import *
import random

window = Tk()
window.geometry('800x900')
# window['background'] = 'light blue'
window.focus_force()
window.resizable(False, False)


" this will be a snake game"


screen_size = 800

# size of a square
grid_size = 80
# number of squares in a row/column
grid_amount = 10 #screen_size/grid_size
snake_color = "#62FF00"
bg_color = "#000000"
apple_color = "#FF0000"
start_pos = [(5,5), (5, 6)]
speed = 400 #milliseconds

score = 0

score_label = Label(window, text='Points: 0', font=('Arial', 40))
score_label.grid(row=0, column=0, sticky=N+S+E+W)

window.grid_rowconfigure(0, weight=1, minsize=100)
window.grid_rowconfigure(1, weight=1, minsize=800)
window.grid_columnconfigure(0, weight=1, minsize=800)

canvas = Canvas(window, width=800, height=800)
canvas['background'] = bg_color
canvas.grid(row=1, column=0, sticky=N+S+E+W)


# Giving title to the gaming window


direction = 'up'

# Display of Points Scored in Game

window.bind('<Left>', 
            lambda event: change_direction('left'))
window.bind('<Right>', 
            lambda event: change_direction('right'))
window.bind('<Up>', 
            lambda event: change_direction('up'))
window.bind('<Down>', 
            lambda event: change_direction('down'))





class Snake():
    def __init__(self, color, grid_size, grid_amount, screen_size, start_pos):
        self.color = color
        self.grid_size = grid_size
        self.grid_amount = grid_amount
        self.screen_size = screen_size
        self.positions:list[tuple[int, int]] = start_pos
        self.squares = []
        for grid_x, grid_y in self.positions:
            square = canvas.create_rectangle(grid_x*grid_size, grid_y*grid_size, grid_x*grid_size+grid_size, grid_y*grid_size+grid_size,
                                             fill=self.color, tag='snake')
            self.squares.append(square)
            
        

class Food():
    def __init__(self, color, grid_size, grid_amount, screen_size):
        self.color = color
        self.grid_size = grid_size
        self.screen_size = screen_size
        self.grid_amount =  grid_amount
        grid_x = random.randint(0, grid_amount-1)
        grid_y = random.randint(0, grid_amount-1)
        self.position:list[tuple[int, int]] = [grid_x, grid_y]
        canvas.create_oval(grid_x*grid_size, grid_y*grid_size, grid_x*grid_size+grid_size, grid_y*grid_size+grid_size, 
                           fill=self.color, 
                           tag="food")
        
        
def next_turn(snake:Snake, food:Food):
 # checks the position of the snake's head
    grid_x, grid_y = snake.positions[0]

    if direction == "up":
        grid_y -= 1
    elif direction == "down":
        grid_y += 1
    elif direction == "left":
        grid_x -= 1
    elif direction == "right":
        grid_x += 1

    snake.positions.insert(0, (grid_x, grid_y))

    square = canvas.create_rectangle(grid_x*grid_size, grid_y*grid_size, grid_x*grid_size+grid_size, grid_y*grid_size+grid_size,
                                             fill=snake.color, tag='snake')
    snake.squares.insert(0, square)

    if grid_x == food.position[0] and grid_y == food.position[1]:

        global score

        score += 1

        score_label.config(text=f"Points:{score}")

        canvas.delete("food")

        food = Food(apple_color, grid_size, grid_amount, screen_size)

    else:

        del snake.positions[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    # if collision of the snake happens then 
    # game over function is called
    if check_collisions(snake):
        game_over()

    else:
        window.after(speed, next_turn, snake, food)   


# Function to control direction of snake
def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

# function to check snake's collision and position
def check_collisions(snake:Snake):

     # Taking the coordinates of the snake head
    grid_x, grid_y = snake.positions[0]

    # The function returns true if the collision occurs
    if grid_x < 0 or grid_x >= grid_amount:
        return True
    elif grid_y < 0 or grid_y >= grid_amount:
        return True

    for body_part in snake.positions[1:]:
        if grid_x == body_part[0] and grid_y == body_part[1]:
            return True

    return False

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, 
                       canvas.winfo_height()/2,
                       font=('consolas', 70), 
                       text="GAME OVER", 
                       fill="red", tag="gameover")


snake = Snake(snake_color, grid_size, grid_amount, screen_size, start_pos)
food = Food(apple_color, grid_size, grid_amount, screen_size)

next_turn(snake, food)



window.mainloop()