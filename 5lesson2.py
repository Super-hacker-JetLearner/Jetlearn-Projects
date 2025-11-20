class binary_search_node():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node:binary_search_node = left_node
        self.right_node:binary_search_node = right_node

        
        
    def InOrderTraversal(self):
        current_list = []
        if self.left_node != None:
            current_list.extend(self.left_node.InOrderTraversal())
        current_list.append(self.value)
        if self.right_node != None:
            current_list.extend(self.right_node.InOrderTraversal())
        
        return current_list
    
    def PreOrderTraversal(self):
        current_list = [self.value]
        if self.left_node != None:
            current_list.extend(self.left_node.InOrderTraversal())
        if self.right_node != None:
            current_list.extend(self.right_node.InOrderTraversal())
        
        return current_list
    
    def PostOrderTraversal(self):
        current_list = []
        if self.left_node != None:
            current_list.extend(self.left_node.InOrderTraversal())
        if self.right_node != None:
            current_list.extend(self.right_node.InOrderTraversal())
            
        current_list.append(self.value)
        
        return current_list
    

    


root = None

    
def insert(root, value):
    if root is None:
        root = binary_search_node(value)
        return root
    if value >= root.value:
        if root.right_node != None:
            root.right_node = value
            return root
        else:
            insert(root.right_node, value)
    else:
        if root.left_node != None:
            root.left_node = value
            return root
        else:
            insert(root.left_node, value)
    
    
    
for i in range(10):
    value = int(input('Enter a value: '))
    root = insert(root, value)
    
    
print(root.InOrderTransversal())
    