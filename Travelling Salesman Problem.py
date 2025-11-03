import numpy as np
import random

# ----- Step 1: Define the cities and distance matrix -----
cities = ['A', 'B', 'C', 'D', 'E']
n = len(cities)

# Distance matrix (symmetric)
distance = np.array([
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
])

# ----- Step 2: Parameters -----
num_ants = 10
num_iterations = 100
alpha = 1       # Influence of pheromone
beta = 2        # Influence of distance heuristic
evaporation = 0.5
Q = 100         # Pheromone deposit factor

# ----- Step 3: Initialization -----
pheromone = np.ones((n, n))
best_distance = float('inf')
best_path = []

# ----- Step 4: Helper Functions -----
def path_length(path):
    total = 0
    for i in range(len(path) - 1):
        total += distance[path[i], path[i + 1]]
    total += distance[path[-1], path[0]]  # return to start
    return total

def probability(from_city, unvisited, pheromone, distance):
    probs = []
    for j in unvisited:
        tau = pheromone[from_city][j] ** alpha
        eta = (1 / distance[from_city][j]) ** beta
        probs.append(tau * eta)
    probs = np.array(probs)
    probs /= probs.sum()
    return probs

# ----- Step 5: Main ACO Loop -----
for iteration in range(num_iterations):
    all_paths = []
    all_lengths = []

    for ant in range(num_ants):
        path = [random.randint(0, n - 1)]
        while len(path) < n:
            current = path[-1]
            unvisited = [i for i in range(n) if i not in path]
            probs = probability(current, unvisited, pheromone, distance)
            next_city = np.random.choice(unvisited, p=probs)
            path.append(next_city)
        all_paths.append(path)
        all_lengths.append(path_length(path))

        # Update best path
        if all_lengths[-1] < best_distance:
            best_distance = all_lengths[-1]
            best_path = path

    # ----- Step 6: Update pheromones -----
    pheromone *= (1 - evaporation)
    for k, path in enumerate(all_paths):
        for i in range(n):
            from_city = path[i]
            to_city = path[(i + 1) % n]
            pheromone[from_city][to_city] += Q / all_lengths[k]

    if (iteration + 1) % 10 == 0:
        print(f"Iteration {iteration + 1}: Best Distance = {best_distance:.2f}")

# ----- Step 7: Final Output -----
best_path_cities = [cities[i] for i in best_path]
best_path_cities.append(best_path_cities[0])  # return to start

print("\n🏆 Best Path Found:")
print(" → ".join(best_path_cities))
print(f"Total Distance: {best_distance:.2f}")
