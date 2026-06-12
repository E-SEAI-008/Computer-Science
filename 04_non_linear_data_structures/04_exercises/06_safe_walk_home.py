# Approach 1

from collections import deque


# Time Complexity: O(m × n)
# Where m × n is the total number of cells in the grid.
# Each cell is added to the deque at most twice — once via a cost-0 edge
# (appendleft) and once via a cost-1 edge (append). Each pop does O(1) work.
# Total: O(m × n).


# Space Complexity: O(m × n)
# The dist table is m × n. The deque holds at most O(m × n) entries
# at any one time. Total auxiliary space: O(m × n).
def can_reach_safe(grid, health):
    # Extract number of rows and columns from the provided grid
    num_rows, num_cols = len(grid), len(grid[0])

    # Create a grid like the provided one, filling it with infinity values
    min_health_lost = [[float("inf")] * num_cols for _ in range(num_rows)]
    # [
    #   [0, 1, inf, inf, inf],  # row 0
    #   [0, inf, inf, inf, inf],  # row 1
    #   [inf, inf, inf, inf, inf],  # row 2
    # ]

    # Health loss at starting position
    min_health_lost[0][0] = 0

    # Creating a queue, filling in the starting position
    queue = deque([(0, 0)])

    # Define all possible moves
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # While there is something in the queue
    while queue:
        # We extract the next tuple in the queue e.g. (0, 0) => cr=0, cc=0
        current_row, current_col = queue.popleft()

        # Check if we reached the last cell (bottom right) and if we have at least 1 health remaining
        if current_row == num_rows - 1 and current_col == num_cols - 1:
            return health - min_health_lost[current_row][current_col] >= 1

        #  Loop through each direction
        for row_offset, col_offset in directions:
            # Define which cell I'm moving to
            next_row, next_col = current_row + row_offset, current_col + col_offset

            # Creating boundaries (keep going with valid move, ignore when moving outside the grid)
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                # Extracting the health cost from the provided grid (value = cost)
                step_cost = grid[next_row][next_col]

                # Calculate total health loss if we would move from the current to the next cell
                health_lost_via_current = (
                    min_health_lost[current_row][current_col] + step_cost
                )

                # We only care about the path if it is cheaper than the best route we already found to that neighbour e.g. 0 < inf
                if health_lost_via_current < min_health_lost[next_row][next_col]:
                    min_health_lost[next_row][next_col] = health_lost_via_current

                    if step_cost == 0:
                        queue.appendleft((next_row, next_col))
                    else:
                        queue.append((next_row, next_col))

    return False


print(can_reach_safe([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1))  # True
print(
    can_reach_safe(
        [
            [0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 0],
        ],
        3,
    )
)  # False
print(can_reach_safe([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5))  # True


# Approach 2
print()

from collections import deque


def can_reach_end_bfs(grid, health):
    m, n = len(grid), len(grid[0])
    visited = [[-1] * n for _ in range(m)]  # max health recorded per cell
    queue = deque()

    start_health = health - grid[0][0]
    if start_health < 1:
        return False

    queue.append((0, 0, start_health))
    visited[0][0] = start_health

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, h = queue.popleft()

        if x == m - 1 and y == n - 1:
            return True  # Successfully reached the target

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_health = h - grid[nx][ny]
                if new_health >= 1 and new_health > visited[nx][ny]:
                    visited[nx][ny] = new_health
                    queue.append((nx, ny, new_health))

    return False


print(can_reach_end_bfs([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1))  # True
print(
    can_reach_end_bfs(
        [
            [0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 0],
        ],
        3,
    )
)  # False
print(can_reach_end_bfs([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5))  # True
