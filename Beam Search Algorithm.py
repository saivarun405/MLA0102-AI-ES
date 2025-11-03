# Beam Search Algorithm Implementation
from collections import deque

# Define the graph as an adjacency list with edge costs
graph = {
    'A': {'B': 2, 'C': 4, 'D': 6},
    'B': {'E': 3, 'F': 5},
    'C': {'G': 2},
    'D': {'H': 1},
    'E': {'I': 4},
    'F': {'J': 3},
    'G': {'K': 2},
    'H': {'L': 4},
    'I': {}, 'J': {}, 'K': {}, 'L': {}
}

# Heuristic function (estimated distance to goal)
heuristic = {
    'A': 8, 'B': 6, 'C': 5, 'D': 7,
    'E': 4, 'F': 3, 'G': 2, 'H': 6,
    'I': 0, 'J': 0, 'K': 0, 'L': 0
}

def beam_search(graph, start, goal, beam_width):
    level = [(start, [start])]  # (node, path)

    while level:
        print(f"\nCurrent Level: {[n for n, _ in level]}")

        # Expand all nodes at this level
        next_level = []
        for node, path in level:
            if node == goal:
                return path
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                next_level.append((neighbor, new_path))

        # Sort by heuristic and keep only top-k (beam width)
        next_level.sort(key=lambda x: heuristic[x[0]])
        level = next_level[:beam_width]

    return None


# Breadth-First Search for comparison
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph[node]:
            queue.append((neighbor, path + [neighbor]))
    return None


# Run the Beam Search and BFS
start_node = 'A'
goal_node = 'I'
beam_width = 2

print("=== Beam Search ===")
beam_path = beam_search(graph, start_node, goal_node, beam_width)
print(f"\nBeam Search Path: {beam_path}")

print("\n=== Breadth-First Search (for comparison) ===")
bfs_path = bfs(graph, start_node, goal_node)
print(f"BFS Path: {bfs_path}")
