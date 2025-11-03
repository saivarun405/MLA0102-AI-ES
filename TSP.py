from itertools import permutations

# Function to calculate the total distance of a given route
def calculate_distance(graph, route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += graph[route[i]][route[i + 1]]
    total_distance += graph[route[-1]][route[0]]  # return to start
    return total_distance

# Function to solve TSP using brute-force
def tsp(graph, cities):
    shortest_distance = float('inf')
    best_route = None

    for route in permutations(cities):
        current_distance = calculate_distance(graph, route)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            best_route = route

    return best_route, shortest_distance

# --- Main Program ---
cities = ['A', 'B', 'C', 'D']
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

best_route, best_distance = tsp(graph, cities)

print("Cities:", cities)
print("Shortest Path:", " -> ".join(best_route) + " -> " + best_route[0])
print("Minimum Distance:", best_distance)
