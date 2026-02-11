import collections

# define the graph
# A -> B, B -> C/D, C -> E, D -> F
graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

# part a: BFS implementation
def bfs_graph(start, goal):
    # queue stuff
    queue = collections.deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()

        # check if we at the goal
        if current_node == goal:
            return path

        # mark the current node as visited
        if current_node not in visited:
            visited.add(current_node)

            # add neighbors to the queue
            for neighbor in graph[current_node]:
                    queue.append((neighbor, path + [neighbor]))
    return None

# test
path_a = bfs_graph('A', 'E')
print(f"Path from A to E with BFS: {path_a}")

# part b: DFS implementation
def dfs_graph(start, goal):
    # stack stuff
    stack = [(start, [start])]
    visited = set()

    while stack:
        current_node, path = stack.pop()

        # check if we at the goal
        if current_node == goal:
            return path

        # mark the current node as visited
        if current_node not in visited:
            visited.add(current_node)

            # add neighbors to the stack
            for neighbor in graph[current_node]:
                    stack.append((neighbor, path + [neighbor]))
    return None

# test
path_b = dfs_graph('A', 'E')
print(f"Path from A to E with DFS: {path_b}")