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

    

length = 100

tower1 = stack(100)
for i in reversed(range(1, length+1)):
    tower1.add(i)

towers = [tower1]

for i in range(length-1):
    towers.append(stack(100))


# def move_blocks(towers:list[stack]):
#     for i in range(1, len(towers)):
#         towers[i].add(towers[0].take())
#     towers[-2].add(towers[-1].take())
#     towers[-1].add(towers[0].take())
#     towers[0].add(towers[-2].take())
#     for i in reversed(range(len(towers)-1, 1, -1)):
#         towers[-1].add(towers[i].take())
#     towers[-1].add(towers[0].take())
    
    # return towers
        
        
def move_blocks(towers:list[stack]):
    for i in reversed(range(1, len(towers))):
        towers[i].add(towers[0].take())
        
    towers[-2].add(towers[-1].take())
    towers[-1].add(towers[0].take())
    towers[0].add(towers[-2].take())
    for i in range(1, len(towers)-1):
        towers[-1].add(towers[i].take())
        
    towers[-1].add(towers[0].take())
    
    return towers
        


print(move_blocks(towers))