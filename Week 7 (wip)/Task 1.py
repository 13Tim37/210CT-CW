class Node(object):
 
    def __init__(self, i):
        self.edges = []
        self.id = i

class Graph(object):

    def __init__(self):
        self.count = 0
        self.nodes = []
        self.edges = []

    def add_node(self):
        node = Node(len(self.nodes)+1)
        self.nodes.append(node)
        return node

    def add_edge(self, node1, node2):
        if [node1, node2] not in self.edges:
            self.edges.append([node1, node2])
        if node2 not in node1.edges:
            node1.edges.append(node2)
        if node1 not in node2.edges:
            node2.edges.append(node1)

    def dfs(self, node):
        visited = []
        stack = []
        stack.append(self.nodes[node])
        while len(stack) > 0:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                for edge in node.edges:
                    stack.append(edge)
                    
        f = open('visited', 'a')
        f.write('Nodes visited via DFS: \n')
        for node in visited:
            f.write(str(node.id) + '\n')
        f.close()
        
        return visited

    def bfs(self, node):
        visited = []
        queue = []
        queue.append(self.nodes[node])
        while len(queue) > 0:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                for edge in node.edges:
                    queue.append(edge)

        f = open('visited', 'a')
        f.write('Nodes visited via BFS: \n')
        for node in visited:
            f.write(str(node.id) + '\n')
        f.close()
                    
        return visited
        
 

if __name__ == '__main__':

    G = Graph()
    a = G.add_node()
    b = G.add_node()
    c = G.add_node()
    d = G.add_node()
    e = G.add_node()
    f = G.add_node()
    g = G.add_node()
    h = G.add_node()
    i = G.add_node()
    
    G.add_edge(a,b)
    G.add_edge(a,i)
    G.add_edge(c,i)
    G.add_edge(g,i)
    G.add_edge(c,d)
    G.add_edge(c,e)
    G.add_edge(c,f)
    G.add_edge(e,h)
    G.add_edge(f,g)
    G.add_edge(h,g)
    
    for node in G.dfs(0):
        print(node.id)

    print('---')

    for node in G.bfs(0):
        print(node.id)

    print('---')
    
    for edge in G.edges:
        for node in edge:
            print(node.id)
        print('-')


