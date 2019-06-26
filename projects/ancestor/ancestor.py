# Breadth-First Search

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # Set

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if v2 not in self.vertices.get(v1):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)


def earliest_ancestor(ancestors, starting_node):
    # Frame the problem as a graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    # Use BFS to determine the earliest ancestor
    max_path_len = 1
    earliest_ancestor = -1
    visited = set()
    q = Queue()
    q.enqueue([starting_node])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if (len(path) == max_path_len and v < earliest_ancestor) or len(path) > max_path_len:
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor