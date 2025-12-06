

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
        
    
    
# my_stack = stack(10)
# for i in range(10):
#     my_stack.add(i)
    
    
    
# print(my_stack.take())

# print(my_stack.take())
    
# print(my_stack.top())
# print(my_stack.top())
    
    
# my_stack.add(11)

# print(my_stack.take())

# print(my_stack.show_full())



# for i in range(10):
#     print(my_stack.top())
    


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
    
    
# my_queue = queue(10)

# for i in range(10):
#     my_queue.enqueue(i)
    
# print(my_queue.dqueue())

# print(my_queue.dqueue())

# print(my_queue.get_rear())

# print(my_queue.show_full())

# print(my_queue.peak())






    



class fake_queue():
    def __init__(self, max_elements):
        self.stack2 = stack()
        self.max_elements = max_elements
        
    def enqueue(self, item):
        if len(self.stack2.list) < self.max_elements:
            self.stack2.add(item)
        else:
            raise Exception(f'queue overflow. queue maximum height exceeded ({self.max_elements})')
        
    def dqueue(self):
        reversed_stack = stack()
        for i in range(len(self.stack2)):
            reversed_stack.add(self.stack2.take())
        item = reversed_stack.take()
        for i in range(len(reversed_stack)):
            self.stack2.add(reversed_stack.take())
        return item
    
    
    def get_rear(self):
        if len(self.stack2) > 0:
            return self.stack2.top()
        else:
            raise Exception('queue is empty. queue has 0 elements.')
        
    def peek(self):
        reversed_stack = stack()
        for i in range(len(self.stack2)):
            reversed_stack.add(self.stack2.take())
        item = reversed_stack.top()
        for i in range(len(reversed_stack)):
            self.stack2.add(reversed_stack.take())
        return item
        
        
    def __len__(self):
        return len(self.stack2.list)
            
                
    def show_full(self):
        return self.stack2.list


"homework: bracket matching, optionally fakequeue, just store everything in one stack, and use other stack temporarily for adding/taking"


fake_queue1 = fake_queue(10)

for i in range(10):
    fake_queue1.enqueue(i)
    
print(fake_queue1.dqueue())
print(fake_queue1.dqueue())

print(fake_queue1.peek())
print(fake_queue1.get_rear())


    
print(fake_queue1.show_full())