from collections import deque, defaultdict


# Approach 1


# Time Complexity: O(V + E)
# Where V is the number of vertices (n) and E is the number of edges. We process each vertex at most once when it is popped from the queue, and we iterate over every edge at most twice (once from each connected vertex) to check neighbors. Building the adjacency list also takes O(E) time.
# Space Complexity: O(V + E) auxiliary space
# The adjacency list requires O(V + E) space to store the graph's connections. Additionally, the queue and the visited boolean array each take O(V) space in the worst case (if the queue holds all nodes at a specific level).
def valid_path_bfs(n, edges, source, destination):
    if source == destination:
        return True

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([source])

    visited = [False] * n
    visited[source] = True

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor == destination:
                return True

            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return False


# Example: n=3, edges=[[0,1],[1,2],[2,0]], source=0, dest=2

# Adjacency list: {0: [1, 2], 1: [0, 2], 2: [1, 0]}

# Initial state:
#   queue = deque([0])
#   visited = [True, False, False]  # Indices 0, 1, 2

# Iteration 1:
#   Pop node = 0
#   Neighbors of 0: [1, 2]
#     - 1 == 2? No. Visited? No → mark visited, add to queue
#     - 2 == 2? YES! ✓

# Return True

# Path found directly from checking neighbors!

print(valid_path_bfs(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(valid_path_bfs(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))


# Approach 2


# Time Complexity: O(V + E)
# Where V is the number of vertices (n) and E is the number of edges. We process each vertex at most once when it is popped from the stack, and evaluate every edge at most twice. Building the adjacency list also takes O(E) time.
# Space Complexity: O(V + E) auxiliary space
# The adjacency list requires O(V + E) space. The explicit stack and the visited boolean array each take O(V) space in the worst case (such as a straight-line graph where all vertices are pushed onto the stack).
def valid_path_dfs(n, edges, source, destination):
    if source == destination:
        return True

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    stack = [source]

    visited = [False] * n
    visited[source] = True

    while stack:
        node = stack.pop()

        for neighbor in graph[node]:
            if neighbor == destination:
                return True

            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    return False


# Same as above, but stack instead of queue

print(valid_path_dfs(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(valid_path_dfs(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
