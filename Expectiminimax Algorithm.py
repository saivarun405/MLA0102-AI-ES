# Expectiminimax Algorithm Demonstration
# Types of nodes: MAX, MIN, and CHANCE

# Define a simple game tree with node types and utilities
class Node:
    def __init__(self, name, node_type, children=None, probabilities=None, value=None):
        self.name = name
        self.node_type = node_type   # "MAX", "MIN", "CHANCE", or "LEAF"
        self.children = children or []
        self.probabilities = probabilities
        self.value = value            # Only for leaf nodes

# Expectiminimax recursive function
def expectiminimax(node):
    if node.node_type == "LEAF":
        return node.value

    elif node.node_type == "MAX":
        # Choose the child with the maximum value
        values = [expectiminimax(child) for child in node.children]
        best_value = max(values)
        print(f"MAX node {node.name} chooses value {best_value} from {values}")
        return best_value

    elif node.node_type == "MIN":
        # Choose the child with the minimum value
        values = [expectiminimax(child) for child in node.children]
        best_value = min(values)
        print(f"MIN node {node.name} chooses value {best_value} from {values}")
        return best_value

    elif node.node_type == "CHANCE":
        # Compute the expected value using probabilities
        values = [expectiminimax(child) for child in node.children]
        expected_value = sum(p * v for p, v in zip(node.probabilities, values))
        print(f"CHANCE node {node.name} expected value = {expected_value:.2f} from {values}")
        return expected_value


# Build the Game Tree
# Example: Root (MAX) → MIN nodes → CHANCE nodes → LEAF nodes

# Leaf nodes with utility values
L1 = Node("L1", "LEAF", value=3)
L2 = Node("L2", "LEAF", value=12)
L3 = Node("L3", "LEAF", value=8)
L4 = Node("L4", "LEAF", value=2)
L5 = Node("L5", "LEAF", value=4)
L6 = Node("L6", "LEAF", value=6)

# Chance nodes (stochastic events with probabilities)
C1 = Node("C1", "CHANCE", [L1, L2], probabilities=[0.7, 0.3])
C2 = Node("C2", "CHANCE", [L3, L4], probabilities=[0.4, 0.6])
C3 = Node("C3", "CHANCE", [L5, L6], probabilities=[0.5, 0.5])

# Min nodes (opponent's move)
M1 = Node("M1", "MIN", [C1, C2])
M2 = Node("M2", "MIN", [C3])

# Root node (Maximizing player)
Root = Node("Root", "MAX", [M1, M2])

# Run Expectiminimax
print("\n--- EXPECTIMINIMAX TREE EVALUATION ---\n")
optimal_value = expectiminimax(Root)
print(f"\n✅ Optimal decision value at the root node: {optimal_value:.2f}")

