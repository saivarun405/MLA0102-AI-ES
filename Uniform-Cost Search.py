import heapq

# Uniform Cost Search implementation
def uniform_cost_search(graph, start, goal):
    # Priority queue → (cost, path)
    pq = [(0, [start])]
    visited = set()

    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]

        # Goal check
        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbour, weight in graph.get(node, []):
                if neighbour not in visited:
                    heapq.heappush(pq, (cost + weight, path + [neighbour]))

    return None, float('inf')

# Dijkstra’s Algorithm for validation
def dijkstra(graph, start, goal):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    parents = {start: None}

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node == goal:
            break

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.insert(0, node)
        node = parents[node]
    return path, distances[goal]

# Weighted Graph Representation (Adjacency List)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 1)],
    'E': [('F', 2)],
    'F': []
}

# Define Start and Goal
start, goal = 'A', 'F'

# Perform UCS
ucs_path, ucs_cost = uniform_cost_search(graph, start, goal)
print("Uniform-Cost Search Result:")
print(f"Optimal Path: {' -> '.join(ucs_path)}")
print(f"Total Cost: {ucs_cost}")

# Validate with Dijkstra’s Algorithm
dijkstra_path, dijkstra_cost = dijkstra(graph, start, goal)
print("\nDijkstra’s Algorithm Result:")
print(f"Shortest Path: {' -> '.join(dijkstra_path)}")
print(f"Total Cost: {dijkstra_cost}")

# Compare for Validation
if ucs_cost == dijkstra_cost:
    print("\n✅ UCS result validated: Both algorithms found the same optimal path.")
else:
    print("\n❌ UCS result differs from Dijkstra’s shortest path.")

