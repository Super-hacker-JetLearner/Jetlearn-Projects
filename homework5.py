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


# root = binary_search_node(5, 'a')
    
    
# for i in range(5):
#     key = int(input('Enter a key: '))
#     value = input('Enter a value: ')
#     root.insert(key, value)
    
    
# print(root.InOrderTraversal())
    
# print(root.find(8))

string = """
Actions
1. create tree
2. insert key & value
3. print inordertraversal
4. print preordertraversal
5. print postordertraversal
6. find value from key
7. quit"""



while True:
    print(string)
    action = int(input('Enter action number: '))
    if action == 1:
        root = binary_search_node()
        print('created tree')
    elif action == 2:
        key = int(input('Enter a key: '))
        value = input('Enter a value: ')
        root.insert(key, value)
    elif action == 3:
        print(root.InOrderTraversal())
    elif action == 4:
        print(root.PreOrderTraversal())
    elif action == 5:
        print(root.PostOrderTraversal())
    elif action == 6:
        key == int(input("Enter key: "))
        print(root.find(key))
    elif action == 7:
        print('exiting')
        exit()
    