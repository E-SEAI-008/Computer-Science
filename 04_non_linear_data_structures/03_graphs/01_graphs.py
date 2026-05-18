print("\n--- Undirected Graph ---\n")


class UndirectedGraph:
    def __init__(self, labels):
        """
        Initialize an undirected graph using the provided vertex labels.

        In an UNDIRECTED graph, edges work both ways - like a two-way street.
        If there's an edge from A to B, you can also travel from B to A.

        Args:
            labels: List of vertex names, e.g., ["A", "B", "C", "D"]

        The adjacency matrix is a 2D grid where:
        - Rows represent "from" vertices
        - Columns represent "to" vertices
        - matrix[i][j] = weight means there's an edge from vertex i to vertex j
        - For undirected graphs: matrix[i][j] = matrix[j][i] (symmetric)
        - 0 means no edge exists between those vertices
        """
        self.labels = labels  # Store vertex names for human-readable output
        self.num_vertices = len(labels)  # Count how many vertices we have
        # Create an n×n matrix filled with zeros (no edges initially)
        # Example for 4 vertices: [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        """
        Convert a vertex label (like "A") to its index position (like 0).

        This helper method lets us use friendly names instead of numbers.
        Example: If labels = ["A", "B", "C"], then "B" → index 1
        """
        if label not in self.labels:
            raise ValueError(f"Label {label} not found in the graph.")
        return self.labels.index(label)

    def add_edge(self, label1, label2, weight=1):
        """
        Add an edge between two vertices in an UNDIRECTED graph.

        KEY CONCEPT: In undirected graphs, we update BOTH directions!
        If we add an edge from A to B, we can also travel from B to A.

        Args:
            label1: First vertex (e.g., "A")
            label2: Second vertex (e.g., "B")
            weight: Edge weight (default 1 for unweighted graphs)

        Example: add_edge("A", "B", 5) creates a connection with weight 5
        - matrix[A][B] = 5  (can go from A to B)
        - matrix[B][A] = 5  (can also go from B to A)
        """
        # Convert labels to matrix indices
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)

        # CRITICAL: Update both directions for undirected graph
        self.adj_matrix[u][v] = weight  # A → B
        self.adj_matrix[v][u] = weight  # B → A (symmetric)

    def remove_edge(self, label1, label2):
        """
        Remove an edge between two vertices in an UNDIRECTED graph.

        Just like adding, we must remove BOTH directions.
        Setting to 0 means "no edge exists".

        Args:
            label1: First vertex
            label2: Second vertex
        """
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)

        # Remove both directions
        self.adj_matrix[u][v] = 0  # Remove A → B
        self.adj_matrix[v][u] = 0  # Remove B → A

    def print_matrix(self):
        """
        Print the adjacency matrix in a readable format.

        Output shows which vertices are connected:
        - Row label = starting vertex
        - Column label = destination vertex
        - Number = edge weight (0 = no edge)
        """
        # Print header row with vertex labels
        header = "   " + "  ".join(self.labels)
        print(header)
        # Print each row with its label
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}  {row_str}")


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

# ------------------------------------------------------------------

print("\n--- Directed Graph ---\n")


class DirectedGraph:
    def __init__(self, labels):
        """
        Initialize a directed graph using the provided vertex labels.

        In a DIRECTED graph, edges are one-way - like a one-way street.
        An edge from A to B does NOT mean you can go from B to A.

        Args:
            labels: List of vertex names, e.g., ["A", "B", "C", "D"]

        The adjacency matrix for directed graphs:
        - matrix[i][j] = weight means there's a directed edge FROM i TO j
        - matrix[i][j] does NOT equal matrix[j][i] (not symmetric)
        - Think of it as: "Can I go from row to column?"

        Example use cases:
        - Social media follows (A follows B doesn't mean B follows A)
        - Web page links (page A links to B, but B might not link back)
        - Task dependencies (task A must complete before B)
        """
        self.labels = labels  # Store vertex names
        self.num_vertices = len(labels)  # Count vertices
        # Create n×n matrix initialized to 0 (no edges)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def label_to_index(self, label):
        """
        Convert a vertex label to its matrix index.

        Same as undirected graph - helps us use names instead of numbers.
        """
        if label not in self.labels:
            raise ValueError(f"Label {label} not found in the graph.")
        return self.labels.index(label)

    def add_edge(self, label_from, label_to, weight=1):
        """
        Add a DIRECTED edge from one vertex to another.

        KEY DIFFERENCE from undirected: We only update ONE direction!

        Args:
            label_from: Source vertex (where the edge starts)
            label_to: Destination vertex (where the edge points)
            weight: Edge weight (default 1)

        Example: add_edge("A", "B", 3) means:
        - There IS an edge from A to B with weight 3
        - There is NO edge from B to A (unless we add it separately)

        Think of it as an arrow: A → B
        """
        # Convert labels to indices
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)

        # CRITICAL: Only update ONE direction for directed graph
        self.adj_matrix[u][v] = weight  # A → B only
        # Notice: We do NOT set matrix[v][u] = weight

    def remove_edge(self, label_from, label_to):
        """
        Remove a DIRECTED edge from one vertex to another.

        Only removes the edge in the specified direction.
        If there's an edge in the opposite direction, it stays.

        Args:
            label_from: Source vertex
            label_to: Destination vertex
        """
        u = self.label_to_index(label_from)
        v = self.label_to_index(label_to)

        # Remove only the specified direction
        self.adj_matrix[u][v] = 0  # Remove A → B
        # Notice: We do NOT touch matrix[v][u]

    def print_matrix(self):
        """
        Print the adjacency matrix for the directed graph.

        Reading the matrix:
        - Find the row for your starting vertex
        - Look across the columns to see where you can go
        - Non-zero values show outgoing edges from that vertex

        Example: If row A has [0, 1, 1, 0], vertex A has edges to B and C
        """
        # Print column headers
        header = "    " + "  ".join(self.labels)
        print(header)
        # Print each row with its label
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]}   {row_str}")


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
