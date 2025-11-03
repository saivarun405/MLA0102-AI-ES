import random

# Function to calculate the number of attacking pairs
def cost(state):
    c = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                c += 1
    return c

# Function to print the board
def print_board(state):
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[j] == i:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# Hill Climbing Algorithm
def hill_climb(n):
    state = [random.randint(0, n - 1) for _ in range(n)]
    while True:
        neighbors = []
        for i in range(n):
            for j in range(n):
                if j != state[i]:
                    new_state = list(state)
                    new_state[i] = j
                    neighbors.append(new_state)
        costs = [cost(nei) for nei in neighbors]
        min_cost = min(costs)
        best = neighbors[costs.index(min_cost)]
        if min_cost >= cost(state):
            break
        state = best
    print_board(state)
    print("Final cost:", cost(state))
    if cost(state) == 0:
        print("✅ Solution found!")
    else:
        print("❌ Local optimum reached!")

# Main
n = int(input("Enter number of queens: "))
hill_climb(n)
