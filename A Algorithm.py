from queue import PriorityQueue

# --- Heuristic function (straight-line distance) ---
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 0
}

# --- Graph represented as adjacency list with weights ---
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('F', 1), ('E', 1)],
    'E': [('F', 2)],
    'F': []
}

# --- A* Search Algorithm ---
def a_star(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    expanded_order = []

    while not open_set.empty():
        current = open_set.get()[1]
        expanded_order.append(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal], expanded_order

        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic[neighbor]
                open_set.put((f_score[neighbor], neighbor))

    return None, float('inf'), expanded_order

# --- Run the algorithm ---
start_node = 'A'
goal_node = 'F'
path, total_cost, expanded_nodes = a_star(start_node, goal_node)

print("Order of node expansion:", expanded_nodes)
print("Optimal Path:", " -> ".join(path))
print("Total Cost:", total_cost)

