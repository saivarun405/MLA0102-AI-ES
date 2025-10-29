from collections import deque
start = (3, 3, 1)
goal = (0, 0, 0)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid(state):
    M_left, C_left, _ = state
    M_right, C_right = 3 - M_left, 3 - C_left

    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False

    if (M_left > 0 and M_left < C_left) or (M_right > 0 and M_right < C_right):
        return False

    return True

def bfs():
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (M_left, C_left, boat), path = queue.popleft()

        if (M_left, C_left, boat) == goal:
            return path

        for m, c in moves:
            if boat == 1:  # Boat on left → move to right
                new_state = (M_left - m, C_left - c, 0)
            else:          # Boat on right → move to left
                new_state = (M_left + m, C_left + c, 1)

            if is_valid(new_state) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None

# Solve
solution = bfs()

# Display result
print("Missionaries and Cannibals Problem Solution:\n")
for step in solution:
    print(step)
