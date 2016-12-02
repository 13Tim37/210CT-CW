class Node(object):
 
    def __init__(self, i):
        self.edges = {}
        self.id = i
        self.tw = None
        self.w = None
        self.pre = None

class Graph(object):

    def __init__(self):
        self.count = 0
        self.nodes = []
        self.edges = []

    def add_node(self):
        node = Node(len(self.nodes)+1)
        self.nodes.append(node)
        return node

    def add_edge(self, node1, node2, weight):
        if [node1, node2] not in self.edges:
            self.edges.append([node1, node2, weight])
        if node2 not in node1.edges:
            node1.edges[node2] = weight
        if node1 not in node2.edges:
            node2.edges[node1] = weight

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

    def djikstra(self, tap, sink):
        visited = []
        node = tap
        for n in self.nodes:
            n.tw = float('inf')
        node.tw = 0
        visited.append(node)
        while node != sink:
            # For all nodes next to current node.
            for u in node.edges:
                # node.edges gives format: edges[node] = weight
                if node.tw + node.edges[u] < u.tw:
                    # If edge weight plus current total weight to current node is less that total weight to neighbor node
                    u.tw = node.tw + node.edges[u]
                    # Set neighbor node total weight to edge weight + total weight to current node.
                    u.pre = node
                    # Previous node to neighbor node is current node.
            visited.append(node)
            m = float('inf')
            for n in node.edges:
                if n not in visited and n.tw < m:
                    node = n
                    m = n.tw

        node = sink
        path = [sink.id]
        while True:
            if node.pre != None:
                path.insert(0,node.pre.id)
                node = node.pre
            else:
                break

        print('Path: ' + str(path))
        
        return sink.tw
                    
if __name__ == '__main__':

    G = Graph()
    a = G.add_node()
    b = G.add_node()
    c = G.add_node()
    d = G.add_node()
    e = G.add_node()
    
    G.add_edge(a,b, 5)
    G.add_edge(b,d, 7)
    G.add_edge(c,d, 4)
    G.add_edge(c,e, 8)
    G.add_edge(d,e, 3)
    
    for node in G.dfs(0):
        print(node.id)

    print('---')

    for node in G.bfs(0):
        print(node.id)

    print(G.djikstra(c,e))


