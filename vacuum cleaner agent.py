import random

# Define grid size
rows, cols = 3, 3

# 0 = clean cell, 1 = dirty cell
grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

# Starting position of vacuum cleaner
pos = [0, 0]

# Display initial grid
print("Initial Room State (0=Clean, 1=Dirty):")
for row in grid:
    print(row)

# Function to print the grid with current position
def print_grid(grid, pos):
    for i in range(rows):
        for j in range(cols):
            if [i, j] == pos:
                print("V", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()
    print()

# Function for vacuum to clean the grid
def vacuum_cleaner(grid, pos):
    moves = 0
    for i in range(rows):
        for j in range(cols):
            pos[0], pos[1] = i, j  # Move vacuum to new position
            print(f"Vacuum moved to position ({i}, {j})")
            moves += 1

            # Clean if dirty
            if grid[i][j] == 1:
                print("Dirty spot found! Cleaning...")
                grid[i][j] = 0
            else:
                print("Already clean.")
            
            print_grid(grid, pos)

    print("Cleaning completed!")
    print("Total moves made:", moves)

# Run the simulation
vacuum_cleaner(grid, pos)
