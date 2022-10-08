# ways to implement graphs
"""
# 1. Adjancency List - []
    # List of neighbors stored in each vertex
    # Pro: Faster and uses less space for Sparse graphs
    # Con: Slower for Dense graphs
# 2. Adjancency Matrix - 2D array
    # Matrix of neighbors stored centrally in Graph object
    # Pro: Faster for Dense graphs
    # Pro: Simpler for Weighted edges
    # Con: uses more space
"""
# Undirected Graph
"""
Relationships are 2 ways.
Used to model social or computer networks.
# Adjacency List will be like
    # A: B, C, E -> A connected to B, C, E
    # B: A, C
    # C: A, B, D, E
    # D: C
    # E: A, C

# Adjacency Matrix - 0: No edge, 1: edge
#       A   B   C   D   E
#   A   0   1   1   0   1
#   B   1   0   1   0   0
#   C   1   1   0   1   1
#   D   0   0   1   0   0
#   E   1   0   1   0   0

# Symmetrical and Diagonal -> if A connected to B, B is also connected to A
# Weighted Edges are used to represent distance or time between nodes
"""

# Directed Graph
"""
relationships are 1 ways
Used to model airplane fligths or bus routes

# Adjacency List will be like
    # A: C -> A is single directionally connected to C
    # B: A
    # C: B, E, ZD
    # D: 
    # E: A

# Adjacency Matrix - 0: No edge, 1: edge
#       A   B   C   D   E
#   A   0   0   1   0   0
#   B   1   0   0   0   0
#   C   0   1   0   1   1
#   D   0   0   0   0   0
#   E   1   0   0   0   0

# Adjacency Matrix in Directed graph will no be symmetrical and diagonal
"""

# Which is Better?
# Dense Graph: (E = edges, V = Vertices)
#   graph where |E| = |V|^2

# Sparse Graph:
#   graph where |E| = |V|


# Adjacency List
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = set()

    def add_neighbor(self, v):
        self.neighbors.add(v)

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbors)))


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
# ord() -> convert chr to unicode
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']
for edge in edges:
    g.add_edge(edge[0], edge[1])

g.print_graph()

print("\n")



# Adjacency Matrix
class Vertex_M:
    def __init__(self, n):
        self.name = n

"""
# vertices - dictionary with vertex_name:vertex_object
# edges - a 2-dimensional list (ie. a matrix) of edges. for an unweighted graph it will contain 0 for no edge and 1 for edge
# edge_indices - a dictionary with vertex_name:list_index(eg. A:0) edges
# add_vertex - updates all three of these attributes
# add_edge only needs to update the edges matrix
"""
class Graph_M:
    vertices = {}
    edges = []
    edges_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex_M) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

            for row in self.edges:
                row.append(0)
            # append a row of zeros to the bottom of the edges matrix
            self.edges.append([0] * (len(self.edges) + 1))
            self.edges_indices[vertex.name] = len(self.edges_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            # edges[row][col]
            self.edges[self.edges_indices[u]][self.edges_indices[v]] = weight
            self.edges[self.edges_indices[v]][self.edges_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        print('', end='\t')
        for v, i in sorted(self.edges_indices.items()):
            print(v, end=' ')
        print(' ')
        for v, i in sorted(self.edges_indices.items()):
            print(v, end='\t')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=' ')

            print(' ')


g = Graph_M()
a = Vertex_M('A')

g.add_vertex(a)
g.add_vertex(Vertex_M('B'))

# ord() -> convert chr to unicode
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex_M(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']
for edge in edges:
    g.add_edge(edge[0], edge[1])

g.print_graph()