"""
Simple graph implementation
"""

from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Add a vertex
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        Steps to accomplish the task:

        # Create an empty queue
        # Add the starting vertex_id to the queue
        # Create an empty set to store visited nodes
        # While the queue is not empty...
            # Dequeue, the first vertex
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add all neighbors to the back of the queue
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size > 0:
            v = queue.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        Steps to accomplish the task:

        # Create an empty stack
        # Add the starting vertex_id to the stack
        # Create an empty set to store visited nodes
        # While the stack is not empty...
            # Destack, the first vertex
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add all neighbors to the back of the stack
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        Check if the node is visited
        If not mark as visited
        if not
            mark as visited
            print
            call dft on each child
        """
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        else:
            return
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        # Create an empty queue
        # Add A PATH TO the starting vertex_id to the queue
        # Create an empty set to store visited nodes
        # While the queue is not empty...
            # Dequeue, the first PATH
            # GRAB THE LAST VERTEX FROM THE PATH
            # CHECK IF ITS THE TARGET
                # IF SO, RETURN THE PATH
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # MAKE A COPY OF THE PATH,  BEFORE ADDING
                # Then add A PTATH TO all neighbors to the back of the queue

        """
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])
        
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v == destination_vertex:
                return path
            elif v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    new_path = [*path, neighbor]
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        s.push([starting_vertex])

        while s.size() > 0:
            path = s.pop()
            v = path[-1]

            if v == destination_vertex:
                return path
            elif v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    new_path = [*path, neighbor]
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited.add(starting_vertex)

            if starting_vertex == destination:
                return [starting_vertex]

            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination, visited)

                if new_path is not None and destination in new_path:
                    return [starting_vertex, *new_path]
        else:
            return

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS: " , graph.dfs(1, 6))
    print("DFS RECUR: ", graph.dfs_recursive(1, 6))
