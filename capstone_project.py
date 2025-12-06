import random
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
            if len(self) > 0:
                if item > self.top():
                    raise Exception('cannot place bigger block on smaller block')
                else:
                    self.list.append(item)
            else:
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
for block in reversed(range(length)):
    tower1.add(block)
print(tower1)
print(tower1.top())
    
def switch(one,two):
    return two,one

def move_blocks(length,tower1:stack,tower2:stack,tower3:stack):
    # finished inititializing
    # for iteration in range(1,length+1):
    #     move_blocks(iteration,tower1,tower2,tower3)
        
    if length == 1:
        tower3.add(tower1.take())
    elif length == 2:
        tower2.add(tower1.take())
        tower3.add(tower1.take())
        tower3.add(tower2.take())
    else:
        building_tower = tower3
        starting_tower = tower1
        other_tower = tower2
        for i in range(1,length-1):
            move_blocks(i,starting_tower,other_tower,building_tower)
            building_tower,other_tower = switch(building_tower,other_tower)
            
            
    print(tower1,tower2,tower3)
            
            
    return tower1,tower2,tower3
            
            
# def move_3_blocks(tower1:stack,tower2:stack,tower3:stack):
#     tower3.add(tower1.)
    
def move_blocks2(length,tower1:stack,tower2:stack,tower3:stack):
    if length == 1:
        tower3.add(tower1.take())
    elif length == 2:
        tower2.add(tower1.take())
        tower3.add(tower1.take())
        tower3.add(tower2.take())
    else:
        move_blocks2(length-1,tower1,tower2,tower3)
        print('first stage',tower1,tower2,tower3)
        tower2.add(tower1.take())
        print('second stage',tower1,tower2,tower3)
        move_blocks2(length-1,tower3,tower1,tower2)
        print('third stage',tower1,tower2,tower3)
        
        
        
    print(tower1,tower2,tower3)
        

        

    
    
    
print(move_blocks2(length,tower1,tower2,tower3))