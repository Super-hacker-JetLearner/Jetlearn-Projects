import random
class graph():
    def __init__(self, value=None, nodes=[]):
        self.value = value
        self.nodes:list[graph] = nodes
        
    
    def get_connected(self):
        return self.nodes
    
    
    




nodes = [graph()]
for i in range(10):
    the_graph = graph(nodes=random.choices(nodes, k=random.randint(1, len(nodes))))
    nodes.append(the_graph)
    

