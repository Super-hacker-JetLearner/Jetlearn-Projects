import random
class binary_search_node():
    def __init__(self, key=None, value=None, left_node=None, right_node=None):
        self.key = key
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def InOrderTraversal(self):
        lst = []
        if self.left_node:
            lst.extend(self.left_node.InOrderTraversal())
        lst.append((self.key, self.value))
        if self.right_node:
            lst.extend(self.right_node.InOrderTraversal())
        return lst

    def PreOrderTraversal(self):
        out = [(self.key, self.value)]
        if self.left_node:
            out.extend(self.left_node.PreOrderTraversal())
        if self.right_node:
            out.extend(self.right_node.PreOrderTraversal())
        return out

    def PostOrderTraversal(self):
        out = []
        if self.left_node:
            out.extend(self.left_node.PostOrderTraversal())
        if self.right_node:
            out.extend(self.right_node.PostOrderTraversal())
        out.append((self.key, self.value))
        return out

    def insert(self, key, value):
        if self.key is None:
            self.key = key
            self.value = value
            return

        if key < self.key:
            if not self.left_node:
                self.left_node = binary_search_node(key, value)
            else:
                self.left_node.insert(key, value)
        else:
            if not self.right_node:
                self.right_node = binary_search_node(key, value)
            else:
                self.right_node.insert(key, value)

    def find(self, key):
        if key == self.key:
            return self.value
        elif key < self.key:
            return self.left_node.find(key) if self.left_node else False
        else:
            return self.right_node.find(key) if self.right_node else False

    def find_successor(self):
        node = self.right_node
        while node.left_node:
            node = node.left_node
        return node
    
    def find_predecessor(self):
        node = self.left_node
        while node.right_node:
            node = node.right_node
        return node

    def delete(self, key, parent=None):
        # this iterates trough the tree until it finds the node
        if key < self.key:
            if self.left_node:
                self.left_node.delete(key, self)
            return
        elif key > self.key:
            if self.right_node:
                self.right_node.delete(key, self)
            return


        if not self.left_node and not self.right_node:
            if parent:
                if parent.left_node is self:
                    parent.left_node = None
                else:
                    parent.right_node = None
            else:
                self.key = None
                self.value = None
            return


        if self.left_node and not self.right_node:
            child = self.left_node
        elif self.right_node and not self.left_node:
            child = self.right_node
        else:
            child = None

        if child:
            if parent:
                if parent.left_node is self:
                    parent.left_node = child
                else:
                    parent.right_node = child
            else:
                self.key = child.key
                self.value = child.value
                self.left_node = child.left_node
                self.right_node = child.right_node
            return


        # can be changed to predecessor, but changes below too
        successor = self.find_successor()
        
        self.key = successor.key
        self.value = successor.value
        self.right_node.delete(successor.key, self)
        # self.left_node.delete(...) if predecessor is used





# root = binary_search_node()


# for i in range(1000):
#     key = random.randint(0, 100)
#     value = chr(random.randint(65, 90))
#     root.insert(key, value)
    
# print(root.InOrderTraversal())
# print(len(root.InOrderTraversal()))

# key = input("Enter a key to delete it: ")

# root.delete(int(key))

# print(root.InOrderTraversal())
# print(len(root.InOrderTraversal()))




string = """
Actions
1. create tree
2. insert key & value
3. print inordertraversal
4. print preordertraversal
5. print postordertraversal
6. find value from key
7. delete node by key
8. quit"""



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
        key = int(input("Enter key to delete: "))
        root.delete(key)
        print('Deleted key')
    elif action == 8:
        print('exiting')
        exit()