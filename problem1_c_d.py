import collections

# Grid layout (0 = open, 1 = wall)
# Row 0 is the top row, Row 6 is the bottom row
grid = [
    [0, 1, 1, 1, 1, 1],  # Row 0
    [0, 0, 0, 0, 0, 0],  # Row 1
    [0, 1, 1, 0, 1, 1],  # Row 2
    [0, 1, 1, 0, 1, 1],  # Row 3
    [0, 1, 0, 0, 1, 1],  # Row 4
    [0, 1, 0, 1, 1, 1],  # Row 5
    [0, 0, 0, 1, 1, 1]   # Row 6
]

start_node = (6, 0)  # Starting at the bottom-left corner
goal_node = (3, 3)  # Goal is at row 3, column 3

# part c: BFS implementation for grid
def bfs_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = collections.deque([(start, [start])])
    visited = {start}

    while queue:
        current_node, path = queue.popleft()

        # check if we at the goal
        if current_node == goal:
            return path

        # explore neighbors (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = current_node[0] + dr, current_node[1] + dc

            # check if the new position is within bounds and not a wall
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
    return None

# test
path_c = bfs_grid(grid, start_node, goal_node)
print(f"Path from {start_node} to {goal_node} with BFS: {path_c}")


# part d: DFS implementation for grid
def dfs_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    stack = [(start, [start])]
    visited = set()

    while stack:
        current_node, path = stack.pop()

        # check if we at the goal
        if current_node == goal:
            return path
        
        if current_node not in visited:
            visited.add(current_node)

            # explore neighbors (up, down, left, right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = current_node[0] + dr, current_node[1] + dc

                # check if the new position is within bounds and not a wall
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    if (nr, nc) not in visited:
                        stack.append(((nr, nc), path + [(nr, nc)]))
    return None

# test
path_d = dfs_grid(grid, start_node, goal_node)
print(f"Path from {start_node} to {goal_node} with DFS: {path_d}")
