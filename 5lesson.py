class node():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node:node = left_node
        self.right_node:node = right_node
        
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
    
    
    


node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)

node1.left_node = node2
node1.right_node = node3
node3.left_node = node4

print(node1.InOrderTraversal())
print(node1.PreOrderTraversal())
print(node1.PostOrderTraversal())