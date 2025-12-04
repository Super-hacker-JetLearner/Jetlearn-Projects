

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
    # def __repr__(self):
    #     return str(self.list)
    
    
"""Homework: Infix to prefix using stack
Input: s = "a*(b+c)/d
Output: abc+*d/"""
    
    
def flatten_list(array):
    flat_list = []
    for item in array:
        if type(item) == list:
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
            
    return flat_list
    
def infix_to_prefix(expression:str):
    elements = []
    current_num = ''
    parantheses_indexes = stack(100)
    operators = ['+', '-', '*', '/']
    for index, char in enumerate(expression):
        if len(parantheses_indexes) == 0:
            if char.isdigit() or char == '.':
                current_num += char
            else:
                if current_num != '':
                    elements.append(current_num)
                    current_num = ''
                    
                if char in operators:
                    elements.append(char)
                    
                if char == '(':
                    parantheses_indexes.add(index)
        else:
            if char == ')':
                sub_expression = expression[parantheses_indexes.take()+1:index+1]
                elements.append(infix_to_prefix(sub_expression))
            elif char == '(':
                parantheses_indexes.add(index)
                
    if current_num != '':
        elements.append(current_num)
          
          
                
            
            
    last_operator = None
    new_elements = []
    for index, thing in enumerate(elements):
        if thing in operators:
            last_operator = thing
        else:
            new_elements.append(thing)
            if last_operator is not None:
                new_elements.append(last_operator)
            last_operator = None
            
            
    
            
    return flatten_list(new_elements)
                
                
    # for thing in elements:
    #     print(thing)
    # return elements
       


            
print(infix_to_prefix("2*(5+7)/8"))