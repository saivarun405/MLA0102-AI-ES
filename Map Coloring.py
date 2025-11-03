# Function to check if the color assignment is safe
def is_safe(graph, color, node, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

# Function to solve map coloring using backtracking
def graph_coloring(graph, m, color, node):
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, node, c):
            color[node] = c
            if graph_coloring(graph, m, color, node + 1):
                return True
            color[node] = 0
    return False

# Function to print solution
def print_solution(color):
    print("Region : Color")
    for i, c in enumerate(color):
        print(f"{i + 1}       : {c}")

# Main program
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

m = 3  # Number of colors
color = [0] * len(graph)

if graph_coloring(graph, m, color, 0):
    print("✅ Solution exists!")
    print_solution(color)
else:
    print("❌ No solution exists with the given number of colors.")
