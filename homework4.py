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




class fake_queue():
    def __init__(self, max_elements):
        self.stack = stack(max_elements)
        self.max_elements = max_elements
    
        
    def enqueue(self, item):
        if len(self.stack) < self.max_elements:
            self.stack.add(item)
        else:
            raise Exception(f'queue overflow. queue maximum height exceeded ({self.max_elements})')
            
    def dqueue(self):
        if len(self.stack) > 0:
            reversed_stack = stack(self.max_elements)
            for i in range(len(self.stack)):
                reversed_stack.add(self.stack.take())
            item = reversed_stack.take()
            for i in range(len(reversed_stack)):
                self.stack.add(reversed_stack.take())
            return item
        else:
            raise Exception('Cannot take item from queue. Queue is empty. Lenght of queue is 0.')
        
    def peek(self):
        if len(self.stack) > 0:
            reversed_stack = stack(self.max_elements)
            for i in range(len(self.stack)):
                reversed_stack.add(self.stack.take())
            item = reversed_stack.top()
            for i in range(len(reversed_stack)):
                self.stack.add(reversed_stack.take())
            return item
        else:
            raise Exception('Cannot take item from queue. Queue is empty. Lenght of queue is 0.')
        
    def get_rear(self):
        if len(self.stack) > 0:
            return self.stack.top()
        else:
           raise Exception('Cannot take item from queue. Queue is empty. Lenght of queue is 0.') 
       
    def __str__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)
        


def match_brackets(brackets:str, possible_brackets:dict[str, str]={'(':')', '[':']', '{':'}'}, max_opening_brackets = 100):
    current_stack = stack(max_opening_brackets)
    for bracket in brackets:
        if bracket in possible_brackets.keys():
            current_stack.add(bracket)
        elif bracket in possible_brackets.values():
            if bracket == possible_brackets[current_stack.take()]:
                pass
            else:
                return False
        else:
            pass
        
    return True




string = '()[]{[]}'
print(match_brackets(string))



fake_queue1 = fake_queue(10)

fake_queue1.enqueue(5)
fake_queue1.enqueue(3)
print(fake_queue1.dqueue())
print(fake_queue1.peek())
fake_queue1.enqueue(7)
print(fake_queue1.get_rear())

print(fake_queue1)

print(len(fake_queue1))