import random
import pygame
import time
from pygame.locals import *
class queue():
    def __init__(self, max_elements):
        self.list = list()
        self.max_elements = max_elements
        
    def enqueue(self, item):
        if len(self.list) < self.max_elements:
            self.list.append(item)
        else:
            raise Exception(f'queue overflow. queue maximum height exceeded ({self.max_elements})')
        
            
    def dqueue(self):
        if len(self.list) > 0:
            return self.list.pop(0)
        else:
            raise Exception('queue is empty. queue has 0 elements.')
        
    def peek(self):
        if len(self.list) > 0:
            return self.list[0]
        else:
            raise Exception('queue is empty. queue has 0 elements.')
        
    def get_rear(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            raise Exception('queue is empty. queue has 0 elements.')
        
    def show_full(self):
        return self.list
    
    
    def __len__(self):
        return len(self.list)
    
    def __str__(self):
        return str(self.list)
    
    
class stack():
    def __init__(self, max_elements):
        self.list = list()
        self.max_elements = max_elements
        
    def add(self, item):
        if len(self.list) < self.max_elements:
            # if len(self) > 0:
            #     if item > self.top():
            #         raise Exception('cannot place bigger block on smaller block')
            #     else:
            #         self.list.append(item)
            # else:
            #     self.list.append(item)
            self.list.append(item)
        else:
            raise Exception(f'Stack overflow. Stack maximum height exceeded ({self.max_elements})')
            
    def take(self):
        if len(self.list) > 0:
            return self.list.pop(-1)
        else:
            raise Exception('Stack is empty. Stack has 0 elements.')
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            raise Exception('Stack is empty. Stack has 0 elements.')
        
    def show_full(self):
        return self.list
    
    def clear(self):
        self.list.clear()
        
    def __len__(self):
        return len(self.list)
    
    def __str__(self):
        return str(self.list)
    def __repr__(self):
        return str(self.list)
    
    
    
# people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# people_queue = queue(100)
# for person in people:
#     people_queue.enqueue(person)
    

# while len(people_queue) > 1:
#     max_time = random.randint(0, 100)

#     for i in range(max_time):
#         people_queue.enqueue(people_queue.dqueue())

#     print(people_queue.dqueue(), 'has the potato!')
    
    
# print(people_queue.peek(), 'has won!')



    

length = 10
tower1 = stack(length)
tower2 = stack(length)
tower3 = stack(length)
for block in range(length, 0,-1):
    tower1.add(block)
print(tower1)
print(tower1.top())
    
print(tower1,tower2,tower3)

game_states = []
game_states_takes = []


# def tower_to_number(tower):
#     global tower1,tower2,tower3
#     dictionary = {tower1:1,tower2:2,tower3:3}
#     return dictionary[tower]

def towers_to_numbers(tower, second_tower):
    global tower1,tower2,tower3
    dictionary = {tower1:0,tower2:1,tower3:2}
    return dictionary[tower], dictionary[second_tower]

    
def move_blocks2(length,starting_tower:stack,other_tower:stack,building_tower:stack):
    global game_states
    if length == 0:
        pass
    elif length == 1:
        building_tower.add(starting_tower.take())
        game_states.append((tuple(tower1.list),tuple(tower2.list),tuple(tower3.list)))
        game_states_takes.append(towers_to_numbers(starting_tower,building_tower))
        # print(('length 1',tower1,tower2,tower3))
    elif length == 2:
        other_tower.add(starting_tower.take())
        game_states.append((tuple(tower1.list),tuple(tower2.list),tuple(tower3.list)))
        game_states_takes.append(towers_to_numbers(starting_tower,other_tower))
        # print(('length 2 phase 1',tower1,tower2,tower3))
        building_tower.add(starting_tower.take())
        game_states.append((tuple(tower1.list),tuple(tower2.list),tuple(tower3.list)))
        game_states_takes.append(towers_to_numbers(starting_tower,building_tower))
        # print(('length 2 phase 2',tower1,tower2,tower3))
        building_tower.add(other_tower.take())
        game_states.append((tuple(tower1.list),tuple(tower2.list),tuple(tower3.list)))
        game_states_takes.append(towers_to_numbers(other_tower,building_tower))
        # print(('length 2 phase 3',tower1,tower2,tower3))
    else:

        
        move_blocks2(length-1,starting_tower,building_tower,other_tower)
        # game_states.append((f'length {length} phase 1',tuple(tower1.list),tuple(tower2.list),tuple(tower3.list)))
        # print((f'length {length} phase 1',tower1,tower2,tower3))
        # print('first stage',tower1,tower2,tower3)
        building_tower.add(starting_tower.take())
        game_states.append((tuple(tower1.list),tuple(tower2.list),tuple(tower3.list)))
        game_states_takes.append(towers_to_numbers(starting_tower,building_tower))
        # print((f'length {length} phase 2',tower1,tower2,tower3))
        # print('second stage',tower1,tower2,tower3)
        move_blocks2(length-1,other_tower,starting_tower,building_tower)
        # game_states.append((f'length {length} phase 3',tuple(tower1.list),tuple(tower2.list),tuple(tower3.list)))
        # print((f'length {length} phase 3',tower1,tower2,tower3))
        # print('third stage',tower1,tower2,tower3)



    return tower1,tower2,tower3




'homework: finish tower of hanoi'

game_states.append((tuple(tower1.list),tuple(tower2.list),tuple(tower3.list)))
# print(('start',tower1,tower2,tower3))

print(move_blocks2(length,tower1,tower2,tower3))

# game_states.append(('end',tuple(tower1.list),tuple(tower2.list),tuple(tower3.list)))
# print(('end',tower1,tower2,tower3))

print(game_states)
print(game_states_takes)


WIDTH, HEIGHT = 1000,600
window = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

border_rect = pygame.rect.Rect((0,0),(WIDTH,HEIGHT))

bottom_line = ((50, 550), (950,550))


towers_x = [150,450,750]



left_x = 150


vertical_lines = [((150,50),(150,550)),((450,50),(450,550)),((750,50),(750,550))]


colors = ['pink','red','orange','yellow','green','turquoise','blue','purple','violet','red']
for index,color in enumerate(colors):
    colors[index] = pygame.colordict.THECOLORS[color]

blocks = []
width_difference = 300/length
block_height = 500/length

tower1p = stack(100)
tower2p = stack(100)
tower3p = stack(100)

for i in range(length):
    x_difference = left_x-i*width_difference/2
    this_block = pygame.rect.Rect((x_difference,i*block_height+block_height),(i*width_difference,block_height))
    color = colors[i]
    blocks.append((this_block,color))


for block,color in reversed(blocks):
    tower1p.add(block)

running = True
current_index = 0
move_time = 1

last_time = time.time()
current_block:pygame.rect.Rect = tower1p.top()

current_direction = [0,-1]


# for block in range(length, 0,-1):
#     tower1p.add(block)

block_position = [current_block.centerx, current_block.bottom]


towers = [tower1p,tower2p,tower3p]

movement_path = []

go_up_y = 50

speed = 10

while running:
    # print(current_index, game_states_takes[current_index])
    clock.tick(60)
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
            
    pygame.draw.rect(window, (255,255,255),border_rect, width=5)
    pygame.draw.line(window, (255,255,255), bottom_line[0],bottom_line[1])
    for i in range(3):
        pygame.draw.line(window, (255,255,255), vertical_lines[i][0], vertical_lines[i][1])
        
    for block,color in blocks:
        pygame.draw.rect(window, color, block)
    
    
    
    starting_tower, ending_tower = towers[game_states_takes[current_index][0]], towers[game_states_takes[current_index][1]]
    y_goal = 550-len(ending_tower)*block_height
    x_goal = towers_x[game_states_takes[current_index][1]]
    x_start = towers_x[game_states_takes[current_index][0]]
    

    # y_start = current_block.bottom
    # x_start = current_block.centerx
    up_distance = go_up_y - block_position[0]
    x_distance = x_goal-block_position[1]
    down_distance = go_up_y - y_goal
    total_distance = up_distance+x_distance+down_distance
    # speed = (time.time()-last_time)/total_distance
    if x_distance < 0:
        direction = -1
    else:
        direction = 1

    block_position[0] += current_direction[0]*speed
    block_position[1] += current_direction[1]*speed
    
    if block_position[1] <= go_up_y:
        current_direction = [direction, 0]
        block_position[1] = go_up_y
        # print('from go up to go side')
    if block_position[0] == x_goal:
        current_direction = [0,1]
        # print('from go side to go down')
    if current_direction[0] > 0 and block_position[0]+speed > x_goal:
        current_direction = [0,1]
        block_position[0] = x_goal
    if current_direction[0] < 0 and block_position[0]+speed < x_goal:
        current_direction = [0,1]
        block_position[0] = x_goal
        
    
    
    # print(speed)
    current_block.centerx, current_block.bottom = block_position
    # print(current_block.center)
    # print(current_block)
    
    if time.time() - last_time > move_time:
        print('update')

        # goal_tower = towers[game_states_takes[current_index][1]]
        # start_tower = towers[game_states_takes[current_index][0]]
        # height_of_tower = len(goal_tower)*block_height+block_height
        # start_tower.take()
        # goal_tower.add(current_block)
        # current_block[0].top = height_of_tower
        # current_block[0].centerx = towers_x[game_states_takes[current_index][1]]
            
        # current_block = towers[game_states_takes[current_index+1][0]].top()
        # current_index += 1
        starting_tower, ending_tower = towers[game_states_takes[current_index][0]], towers[game_states_takes[current_index][1]]
        this_block = starting_tower.take()
        height_of_tower = 550-len(ending_tower)*block_height
        this_block.bottom = height_of_tower
        this_block.centerx = towers_x[game_states_takes[current_index][1]]
        
        ending_tower.add(this_block)
        
        
        current_direction = [0,-1]
        current_block = towers[game_states_takes[current_index+1][0]].top()
        current_index += 1
        
        block_position = [current_block.centerx, current_block.bottom]
        y_goal = 550-(len(towers[game_states_takes[current_index][1]])*block_height)
        # y_goal = towers[game_states_takes[current_index+1][1]].top().top
        x_goal = towers_x[game_states_takes[current_index][1]]
        x_start = towers_x[game_states_takes[current_index][0]]
        
        print(y_goal)
        # y_start = current_block.bottom
        # x_start = current_block.centerx
        up_distance = go_up_y - block_position[1]
        x_distance = x_goal-block_position[0]
        down_distance = go_up_y - y_goal
        total_distance = abs(up_distance)+abs(x_distance)+abs(down_distance)
        print(down_distance)
        print(total_distance)
        if total_distance != 0:
            frames = (time.time()-last_time)*60
            print('frames', frames)
            speed = abs(total_distance/frames)
        else:
            speed = 10
            
        last_time = time.time()


    if current_index == len(game_states)-1:
        running = False        
    pygame.display.update()