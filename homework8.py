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
    
    
class graph():
    def __init__(self, vertices:list=[], connections=None, edges=None):
        self.vertices = vertices
        if connections is not None:
            self.connections = connections
        elif edges is not None:
            self.connections = {}
            for start, end in edges:
                if start in self.connections:
                    self.connections[start].append(end)
                else:
                    self.connections[start] = [end]
                    
                if end in self.connections:
                    self.connections[end].append(start)
                else:
                    self.connections[end] = [start]
                    
        
        
    def BFS(self, root=None, queue_max=100):
        if root is None:
            root = self.vertices[0]
            
        node_queue = queue(queue_max)
        visited = []
        node_queue.enqueue(root)
        while len(node_queue) > 0:
            first_node = node_queue.dqueue()
            if first_node not in visited:
                visited.append(first_node)
                
                for connected_node in self.connections[first_node]:
                    node_queue.enqueue(connected_node)
                    
        return visited
    
    def DFS(self, root=None, queue_max=100):
        if root is None:
            root = self.vertices[0]
            
        node_stack = stack(queue_max)
        visited = []
        node_stack.add(root)
        while len(node_stack) > 0:
            first_node = node_stack.take()
            if first_node not in visited:
                visited.append(first_node)
                for connected_node in self.connections[first_node]:
                    node_stack.add(connected_node)
                    
        return visited
    
    
    def find_BFS(self, find, root=None, queue_max=100):
        if root is None:
            root = self.vertices[0]
            
        node_queue = queue(queue_max)
        visited = []
        node_queue.enqueue((root, 0))
        
        while len(node_queue) > 0:
            first_node, distance = node_queue.dqueue()
            if first_node == find:
                return distance
            if first_node not in visited:
                visited.append(first_node)
                
                for connected_node in self.connections[first_node]:
                    node_queue.enqueue((connected_node, distance+1))
                    
        return None
    
    
    def check_edge(self, edge):
        if edge[0] in self.connections:
            if edge[1] in self.connections[edge[0]]:
                return True
            
        return False
    

    
    def get_connections2(self):
        unique_outputs = set()
        for node in self.vertices:
            result = self.BFS(node)
            unique_outputs.add(tuple(sorted(result)))
            
        return unique_outputs
    
    
    
    def check_loop(self, root=None, queue_max=100):
        if root is None:
            root = self.vertices[0]
            
        node_queue = queue(queue_max)
        visited = []
        parent = None
        node_queue.enqueue((root, parent))
        while len(node_queue) > 0:
            first_node, parent = node_queue.dqueue()
            if first_node not in visited:
                visited.append(first_node)
                
                for connected_node in self.connections[first_node]:
                    if connected_node != parent:
                        node_queue.enqueue((connected_node,first_node))
            else:
                return True
                    
        return False






# vertices = [1,2,3,4,5,6,7, 100,101,102]
# # connections = {1:[2, 3], 2:[5, 4, 1], 3:[1, 5], 4:[2], 5:[2, 3]}

# edges = [(1,2), (1,3), (1, 4), (4,5), (5,6), (5,7), (100,101), (100,102)]
# vertices = [0,1,2,3,4,5,7]
# edges = [(0,1),(0,2),(0,3),(1,4),(1,6),(2,5),(3,7),(1,6),(6,5)]
# vertices = [1,2,3]
# edges = [(1,2),(2,3)]
vertices = [1,2,3,4,5]
edges = [(1,2),(1,3),(2,4),(2,5)]


this_graph = graph(vertices, edges=edges)


print(this_graph.BFS())
print(this_graph.DFS())

print(this_graph.check_loop())


# print(this_graph.find_BFS(2))

# print(this_graph.check_edge((6,7)))


"display the connected components in the graph. e.g: edges=[(0,1), (2,3), (2,4)] should return [[0,1], [2,3,4]]"
# print(this_graph.get_connections2())