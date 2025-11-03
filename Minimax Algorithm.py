# Minimax algorithm for a perfect binary tree

def minimax(depth, nodeIndex, isMaximizingPlayer, scores, height):
    # Base case: return the value of the leaf node
    if depth == height:
        return scores[nodeIndex]
    
    # If current move is maximizing
    if isMaximizingPlayer:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, scores, height)
        )
    else:
        # Minimizing player
        return min(
            minimax(depth + 1, nodeIndex * 2, True, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, scores, height)
        )

# Main Program
import math

# Example: leaf nodes (final states)
scores = [3, 5, 2, 9]  # Values at the 4 leaves
height = math.log2(len(scores))  # Height of the tree

# Find the best value for the maximizing player
best_value = minimax(0, 0, True, scores, int(height))

print("Leaf node scores:", scores)
print("The optimal value for the Maximizing Player is:", best_value)
