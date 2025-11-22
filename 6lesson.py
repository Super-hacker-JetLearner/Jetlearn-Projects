class binary_search_node():
    def __init__(self, key=None, value=None, left_node=None, right_node=None):
        self.key = key
        self.value = value
        self.left_node:binary_search_node = left_node
        self.right_node:binary_search_node = right_node
        
        
        
    def InOrderTraversal(self):
        current_list = []
        if self.left_node != None:
            current_list.extend(self.left_node.InOrderTraversal())
        current_list.append((self.key, self.value))
        if self.right_node != None:
            current_list.extend(self.right_node.InOrderTraversal())
        
        return current_list
    
    def PreOrderTraversal(self):
        current_list = [(self.key, self.value)]
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
            
        current_list.append((self.key, self.value))
        
        return current_list

        
        
    
    def insert(self, key, value):
        if self.key == None:
            self.key = key
            self.value = value
            return
        if key < self.key:
            if self.left_node == None:
                self.left_node = binary_search_node(key, value)
            else:
                self.left_node.insert(key, value)
        else:
            if self.right_node == None:
                self.right_node = binary_search_node(key, value)
            else:
                self.right_node.insert(key, value)
    

    def find(self, key):
        if key == self.key:
            return self.value
        elif key < self.key:
            if self.left_node != None:
                return self.left_node.find(key)
            else:
                return False
        else:
            if self.right_node != None:
                return self.right_node.find(key)
            else:
                return False




def find_give_node(root:binary_search_node, key, parent=None):
        if key == root.key:
            return root, parent
        elif key < root.key:
            if root.left_node != None:
                return find_give_node(root.left_node, key, root)
            else:
                return False
        else:
            if root.right_node != None:
                return find_give_node(root.right_node, key, root)
            else:
                return False


def binary_search3(the_list:list, find):
    current_range = (0, len(the_list))
    while the_list[current_range[0]:current_range[1]]:
        print('loop')
        # print(the_list[current_range[0]:current_range[1]])
        range = current_range[1] - current_range[0]
        half = range//2
        real_half = current_range[0]+half
        item = the_list[real_half]
        if find == item:
            return real_half
        elif find > item:
            current_range = (real_half, current_range[1])
        elif find < item:
            current_range = (current_range[0], real_half)



def find_successor(root:binary_search_node):
    if root.left_node != None:
        return find_successor(root.left_node)
    else:
        return root


def delete(root:binary_search_node, key):
    the_node = find_give_node(root, key)
    if the_node is False:
        return False
    
    the_node, parent = the_node
    
    if the_node.right_node is None and the_node.left_node is None:
        if parent.right_node == the_node:
            parent.right_node = None
        if parent.left_node == the_node:
            parent.left_node = None
            
        del the_node
        return
    elif the_node.right_node is None:
        if parent.right_node == the_node:
            parent.right_node = the_node.left_node
        if parent.left_node == the_node:
            parent.left_node = the_node.left_node
        del the_node
        return
    elif the_node.left_node is None:
        if parent.right_node == the_node:
            parent.right_node = the_node.right_node
        if parent.left_node == the_node:
            parent.left_node = the_node.right_node
        del the_node
        return
    else:
        
    
        successor = find_successor(the_node.right_node)
        
        the_node.key = successor.key
        the_node.value = successor.value
        delete(the_node, successor.key)
    
    

    
    
    
    
root = binary_search_node()

for i in range(10):
    root.insert(int(input('Enter a key: ')), input('Enter a value: '))
    
print(root.InOrderTraversal())

key = int(input('Enter the key of the thing you want to delete: '))
delete(root, key)
 
print(root.InOrderTraversal())               
       
            