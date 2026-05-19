print("\n--- DFS Graph Traversal (Undirected) ---\n")


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

    def dfs(self, start_label):
        """
        Perform DFS traversal starting from the vertex with label 'start_label'.

        DFS explores as far as possible along each branch before backtracking.
        It uses recursion (which implicitly uses the call stack) to remember
        where to return after exploring a branch.
        """
        # Track which vertices we've already visited to avoid cycles
        visited = set()

        def dfs_helper(label):
            """
            Recursive helper function that performs the actual DFS traversal.

            Args:
                label: The label of the current vertex to visit
            """
            # Step 1: Visit the current vertex (process it)
            print(label)
            # Step 2: Mark it as visited so we don't visit it again
            visited.add(label)

            # Step 3: Get the index of the current vertex in the adjacency matrix
            start_index = self.label_to_index(label)

            # Step 4: Explore all adjacent vertices (neighbors)
            # enumerate gives us both the index and the value (is_connected)
            for neighbor_index, is_connected in enumerate(self.adj_matrix[start_index]):
                # Get the label of this potential neighbor
                neighbor_label = self.labels[neighbor_index]

                # Step 5: If there's an edge (is_connected is non-zero)
                # AND the neighbor hasn't been visited yet, recurse into it
                # This is where we "go deep" - we immediately explore this neighbor
                # before checking other neighbors of the current vertex
                if is_connected and neighbor_label not in visited:
                    dfs_helper(neighbor_label)

            # Step 6: When we reach here, all neighbors have been explored
            # The function returns and we backtrack to the previous vertex

        # Start the DFS traversal from the given starting vertex
        dfs_helper(start_label)


# Define vertex labels
labels = ["A", "B", "C", "D"]

# Create an undirected graph with these labels
graph = UndirectedGraph(labels)

# Add some edges between the vertices
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C")

print("Adjacency Matrix of the Undirected Graph:")
graph.print_matrix()

print("\nDFS traversal starting from vertex A:")
graph.dfs("A")

# -----------------------------------------------------------------------------------------

print("\n--- BFS Graph Traversal (Undirected) ---\n")


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

    def bfs(self, start_label):
        """
        Perform BFS traversal starting from the vertex with label 'start_label'.

        BFS explores the graph level by level, visiting all neighbors at the
        current level before moving to the next level. It uses a queue (FIFO)
        to keep track of which vertices to visit next.
        """
        # Track which vertices we've already visited to avoid cycles
        visited = set()
        # Use a list as a queue (FIFO - First In, First Out)
        # Note: For better performance with large graphs, use collections.deque
        queue = []

        # Step 1: Start with the initial vertex
        # Add it to the queue and mark it as visited immediately
        queue.append(start_label)
        visited.add(start_label)

        # Step 2: Process vertices until the queue is empty
        while queue:
            # Step 3: Dequeue the front vertex (FIFO - remove from front)
            # pop(0) removes and returns the first element
            current_label = queue.pop(0)
            # Step 4: Process/visit this vertex
            print(current_label)

            # Step 5: Get the index of the current vertex in the adjacency matrix
            current_index = self.label_to_index(current_label)

            # Step 6: Enqueue all unvisited adjacent vertices (neighbors)
            # This is where we explore "level by level" - we add all neighbors
            # to the queue before processing any of them
            for neighbor_index, is_connected in enumerate(
                self.adj_matrix[current_index]
            ):
                # Get the label of this potential neighbor
                neighbor_label = self.labels[neighbor_index]

                # Step 7: If there's an edge (is_connected is non-zero)
                # AND the neighbor hasn't been visited yet
                if is_connected and neighbor_label not in visited:
                    # Add the neighbor to the queue for later processing
                    queue.append(neighbor_label)
                    # Mark it as visited NOW (not when we dequeue it)
                    # This prevents adding the same vertex multiple times
                    visited.add(neighbor_label)

            # Step 8: Loop continues - dequeue the next vertex and repeat
            # This ensures we process all vertices at the current level
            # before moving to the next level


# Define vertex labels
labels = ["A", "B", "C", "D"]

# Create an undirected graph with these labels
graph = UndirectedGraph(labels)

# Add some edges between the vertices
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C")

print("Adjacency Matrix of the Undirected Graph:")
graph.print_matrix()

print("\nBFS traversal starting from vertex A:")
graph.bfs("A")

# -----------------------------------------------------------------------------------------

print("\n--- DFS Graph Traversal (Directed) ---\n")


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

    def dfs(self, start_label):
        """Perform DFS traversal starting from the vertex with label 'start_label'."""
        visited = set()

        def dfs_helper(label):
            print(label)
            visited.add(label)
            start_index = self.label_to_index(label)

            for neighbor_index, is_connected in enumerate(self.adj_matrix[start_index]):
                neighbor_label = self.labels[neighbor_index]
                if is_connected and neighbor_label not in visited:
                    dfs_helper(neighbor_label)

        dfs_helper(start_label)


# Define vertex labels
labels = ["A", "B", "C", "D"]

# Create a directed graph with these labels
graph = DirectedGraph(labels)

# Add directed edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("D", "A")

print("Adjacency Matrix of the Directed Graph")
graph.print_matrix()

print("\nDFS traversal starting from vertex A:")
graph.dfs("A")

# -----------------------------------------------------------------------------------------

print("\n--- BFS Graph Traversal (Directed) ---\n")


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

    def bfs(self, start_label):
        visited = set()
        queue = []

        queue.append(start_label)
        visited.add(start_label)

        while queue:
            current_label = queue.pop(0)
            print(current_label)

            current_index = self.label_to_index(current_label)

            for neighbor_index, is_connected in enumerate(
                self.adj_matrix[current_index]
            ):
                neighbor_label = self.labels[neighbor_index]
                if is_connected and neighbor_label not in visited:
                    queue.append(neighbor_label)
                    visited.add(neighbor_label)


# Define vertex labels
labels = ["A", "B", "C", "D"]

# Create a directed graph with these labels
graph = DirectedGraph(labels)

# Add directed edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("D", "A")

print("Adjacency Matrix of the Directed Graph")
graph.print_matrix()

print("\nBFS traversal starting from vertex A:")
graph.bfs("A")
