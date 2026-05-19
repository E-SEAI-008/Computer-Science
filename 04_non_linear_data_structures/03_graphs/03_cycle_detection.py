print("\n--- DFS Cycle Detection (Undirected) ---\n")


class UndirectedGraph:
    def __init__(self, labels):
        self.labels = labels  # e.g., ["A", "B", "C", "D"]
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} not found in the graph.")
        return self.labels.index(label)

    def add_edge(self, label1, label2, weight=1):
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight

    def remove_edge(self, label1, label2):
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    def print_matrix(self):
        header = "   " + "  ".join(self.labels)
        print(header)
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}  {row_str}")

    def detect_cycle_dfs(self):
        """
        Detect if there's a cycle in the undirected graph using DFS.

        In an undirected graph, a cycle exists when we encounter a visited vertex
        that is NOT the direct parent (the vertex we just came from).

        Returns:
            True if a cycle is found, False otherwise.
        """
        # Track which vertices have been visited during the entire traversal
        visited = [False] * self.num_vertices

        # Helper function for DFS traversal
        def dfs(curr, parent):
            """
            Recursively explore the graph to detect cycles.

            Args:
                curr: Index of the current vertex being explored
                parent: Index of the parent vertex (where we came from)
                        -1 means no parent (starting vertex)

            Returns:
                True if a cycle is detected, False otherwise
            """
            # Mark the current vertex as visited
            visited[curr] = True

            # Explore all neighbors of the current vertex
            for neighbor in range(self.num_vertices):
                # Check if there's an edge between curr and neighbor
                if self.adj_matrix[curr][neighbor] != 0:  # There's an edge

                    if not visited[neighbor]:
                        # Case 1: Neighbor hasn't been visited yet
                        # Recurse deeper into this neighbor
                        # Pass curr as the parent for the next call
                        if dfs(neighbor, curr):
                            return True  # Cycle found in deeper recursion

                    elif neighbor != parent:
                        # Case 2: Neighbor has been visited AND it's not our parent
                        # This means we've found a "back edge" to a previously visited vertex
                        # In an undirected graph, this indicates a cycle
                        #
                        # Why check "neighbor != parent"?
                        # In undirected graphs, if we came from A to B, there's an edge B->A
                        # We must ignore this edge back to our parent, or every edge looks like a cycle
                        return True

            # No cycle found from this vertex
            return False

        # Try DFS from each unvisited vertex
        # This handles disconnected graphs (multiple components)
        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                # Start DFS from this vertex with no parent (-1)
                if dfs(vertex, -1):
                    return True  # Cycle found in this component

        # No cycle found in any component
        return False


labels = ["A", "B", "C", "D"]
graph = UndirectedGraph(labels)

# Add edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C")  # This creates a cycle (A-B-C-A)

print("Adjacency Matrix of the Undirected Graph:")
graph.print_matrix()

if graph.detect_cycle_dfs():
    print("Cycle detected in the undirected graph!")
else:
    print("No cycle found in the undirected graph.")

# -----------------------------------------------------------------------------------------

print("\n--- DFS Cycle Detection (Directed) ---\n")


class DirectedGraph:
    def __init__(self, labels):
        self.labels = labels
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        if label not in self.labels:
            raise ValueError(f"Label {label} not found in the graph.")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = weight

    def remove_edge(self, label_from, label_to):
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)
        self.adj_matrix[u][v] = 0

    def print_matrix(self):
        header = "    " + "  ".join(self.labels)
        print(header)
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}   {row_str}")

    def detect_cycle_dfs(self):
        """
        Detect if there's a cycle in the directed graph using DFS.

        In a directed graph, a cycle exists when we encounter a vertex that is
        currently in the recursion stack (active path). This is called a "back edge".

        Key difference from undirected: We need TWO tracking arrays:
        - visited: tracks all vertices we've ever seen
        - rec_stack: tracks vertices in the CURRENT path only

        Returns:
            True if a cycle is found, False otherwise.
        """
        # Track which vertices have been visited during the entire traversal
        visited = [False] * self.num_vertices

        # Track which vertices are in the CURRENT recursion path
        # This is the key difference from undirected cycle detection
        rec_stack = [False] * self.num_vertices

        def dfs(curr):
            """
            Recursively explore the graph to detect cycles.

            Args:
                curr: Index of the current vertex being explored

            Returns:
                True if a cycle is detected, False otherwise
            """
            # Mark the current vertex as visited
            visited[curr] = True
            # Add the current vertex to the recursion stack (active path)
            rec_stack[curr] = True

            # Explore all neighbors of the current vertex
            for neighbor in range(self.num_vertices):
                # Check if there's a directed edge from curr to neighbor
                if self.adj_matrix[curr][neighbor] != 0:

                    if not visited[neighbor]:
                        # Case 1: Neighbor hasn't been visited yet
                        # Recurse deeper into this neighbor
                        if dfs(neighbor):
                            return True  # Cycle found in deeper recursion

                    elif rec_stack[neighbor]:
                        # Case 2: Neighbor has been visited AND is in the current path
                        # This is a "back edge" - we've found a cycle!
                        #
                        # Example: A -> B -> C -> A
                        # When at C, we see edge to A, and A is still in rec_stack
                        #
                        # Why not just check "visited"?
                        # Because a visited vertex might be from a completely finished path
                        # Example: A -> B, A -> C -> D
                        # When exploring C->D, B is visited but not in our current path
                        # Only vertices in rec_stack indicate a cycle
                        return True

            # Done exploring this vertex - remove it from the recursion stack
            # This is crucial! When we backtrack, this vertex is no longer in the active path
            rec_stack[curr] = False
            return False

        # Try DFS from each unvisited vertex
        # This handles disconnected graphs (multiple components)
        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                # Start DFS from this vertex
                if dfs(vertex):
                    return True  # Cycle found in this component

        # No cycle found in any component
        return False


labels = ["A", "B", "C", "D"]
graph = DirectedGraph(labels)

# Add directed edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")  # This creates a cycle (A -> B -> C -> D -> A)

print("Adjacency Matrix of the Directed Graph:")
graph.print_matrix()

if graph.detect_cycle_dfs():
    print("Cycle detected in the directed graph!")
else:
    print("No cycle found in the directed graph.")
