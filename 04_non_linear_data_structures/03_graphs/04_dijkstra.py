print("\n--- Dijkstra's Algorithm (Undirected) ---\n")


class UndirectedGraph:
    def __init__(self, labels):
        self.labels = labels
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


# Create an undirected graph with these labels
labels = ["A", "B", "C", "D", "E", "F"]
graph = UndirectedGraph(labels)
matrix = [
    [0, 4, 5, 0, 0, 0],
    [4, 0, 11, 9, 7, 0],
    [5, 11, 0, 0, 3, 0],
    [0, 9, 0, 0, 13, 2],
    [0, 7, 3, 13, 0, 6],
    [0, 0, 0, 2, 6, 0],
]
# Populate the graph's adjacency matrix directly for demonstration
graph.adj_matrix = matrix
print("Adjacency Matrix of the Undirected Graph:")
graph.print_matrix()


# Dijkstra's Algorithm Implementation
def dijkstra(graph, start_label):
    """
    Compute shortest paths from 'start_label' to all other vertices
    in a graph with non-negative edge weights.
    Returns a dictionary: { label: cost }
    """
    # INITIALIZATION PHASE
    # --------------------
    labels = graph.labels
    n = graph.num_vertices

    # dist[i] = shortest known distance from start to vertex i
    # We use float('inf') to represent "no path found yet"
    dist = [float("inf")] * n

    # visited[i] = True means we've found the optimal path to vertex i
    # Once visited, a vertex is never reconsidered (greedy guarantee)
    visited = [False] * n

    # Set starting vertex distance to 0 (distance from A to A is 0)
    start_index = labels.index(start_label)
    dist[start_index] = 0

    # MAIN LOOP: Process each vertex exactly once
    # -------------------------------------------
    for _ in range(n):
        # STEP 1: GREEDY SELECTION
        # Find the unvisited vertex with the smallest known distance
        # This is the "closest" unvisited vertex we know about

        # min_dist tracks the smallest distance value we've seen
        # min_vertex tracks WHICH vertex has that distance (its index)
        # We use -1 as a sentinel value meaning "no vertex found yet"
        # (Could also use None for more Pythonic code)
        min_dist = float("inf")
        min_vertex = -1

        for i in range(n):
            # Only consider unvisited vertices
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]  # Update the best distance found
                min_vertex = i  # Remember WHICH vertex has this distance

        # If no unvisited vertex is reachable, we're done early
        # (min_vertex stays -1 if we never found a reachable vertex)
        if min_vertex == -1:
            break

        # STEP 2: MARK AS VISITED
        # We've now found the shortest path to this vertex
        # It will never be updated again (Dijkstra's guarantee)
        visited[min_vertex] = True

        # STEP 3: EDGE RELAXATION
        # Check all neighbors of the current vertex
        # See if going through current vertex gives a shorter path
        for neighbor in range(n):
            weight = graph.adj_matrix[min_vertex][neighbor]

            # Only consider edges that exist (weight > 0) and unvisited neighbors
            if weight > 0 and not visited[neighbor]:
                # Calculate: distance to current + edge weight
                new_dist = dist[min_vertex] + weight

                # If this path is shorter than what we knew before, update it
                # This is called "relaxing" the edge
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist

    # RESULT FORMATTING
    # -----------------
    # Convert the distance array to a more readable dictionary format
    # Use None for unreachable vertices (those still at infinity)
    result = {}
    for i, label in enumerate(labels):
        result[label] = dist[i] if dist[i] != float("inf") else None
    return result


# Run Dijkstra from 'A'
print("Shortest path costs from A:\n", dijkstra(graph, "A"))
