# Problem 2
def dls_grid(grid, start, goal, limit):
    rows, cols = len(grid), len(grid[0])
    
    stack = [(start, [start])]
    nodes_expanded = 0

    while stack:
       
        current_node, path = stack.pop()
        nodes_expanded += 1
        
        current_depth = len(path) - 1

        # Goal check
        if current_node == goal:
            return path, nodes_expanded

        # If we are within the depth limit, explore neighbors
        if current_depth < limit:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = current_node[0] + dr, current_node[1] + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    # Avoid cycles to prevent infinite loops
                    if (nr, nc) not in path:
                        stack.append(((nr, nc), path + [(nr, nc)]))
    
    return None, nodes_expanded

# Grid layout (0 = open, 1 = wall)
grid = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1]
]

start_node = (6, 0)
goal_node = (3, 3)

# Run with limit = 4
path_4, nodes_4 = dls_grid(grid, start_node, goal_node, 4)
print(f"--- DLS Limit = 4 ---")
print(f"Path Found: {path_4}")
print(f"Nodes Expanded: {nodes_4}")

# Run with limit = 8
path_8, nodes_8 = dls_grid(grid, start_node, goal_node, 8)
print(f"--- DLS Limit = 8 ---")
print(f"Path Found: {path_8}")
print(f"Nodes Expanded: {nodes_8}")