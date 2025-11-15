

class stack():
    def __init__(self):
        self.list = list()
        self.max_elements = 10
        
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
        
    
    
# my_stack = stack()
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
    def __init__(self):
        self.list = list()
        self.max_elements = 10
        
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
        
    def peak(self):
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
    
    
# my_queue = queue()

# for i in range(10):
#     my_queue.enqueue(i)
    
# print(my_queue.dqueue())

# print(my_queue.dqueue())

# print(my_queue.get_rear())

# print(my_queue.show_full())

# print(my_queue.peak())






    



class fake_queue():
    def __init__(self):
        self.stack2 = stack()
        self.max_elements = 10
        
    def enqueue(self, item):
        if len(self.stack2.list) < self.max_elements:
            this_stack = stack
            
            self.stack2.clear()
            while True:
                try:
                    self.stack2.add(self.stack1.take())
                except:
                    break
        else:
            raise Exception(f'queue overflow. queue maximum height exceeded ({self.max_elements})')
        
            
    def dqueue(self):
        if len(self.stack2.list) > 0:
            return self.stack2.take()
        else:
            raise Exception('queue is empty. queue has 0 elements.')
        
    def peak(self):
        if len(self.stack2.list) > 0:
            return self.stack2.top()
        else:
            raise Exception('queue is empty. queue has 0 elements.')
        
    def get_rear(self):
        if len(self.stack2.list) > 0:
            self.stack1.clear()
            while True:
                try:
                    self.stack1.add(self.stack2.top())
                except:
                    break
            return self.stack1.top()
        else:
            raise Exception('queue is empty. queue has 0 elements.')
        
    def show_full(self):
        self.stack1.clear()
        while True:
            try:
                self.stack1.add(self.stack2.top())
            except:
                break
            
        return self.stack1.list
    
    

fake_queue1 = fake_queue()
for i in range(10):
    fake_queue1.enqueue(i)
    
print(fake_queue1.dqueue())
