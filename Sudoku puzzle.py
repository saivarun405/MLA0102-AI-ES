# Sudoku Solver using Backtracking and Constraint Satisfaction

# Function to print Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Check if placing 'num' is valid at grid[row][col]
def is_valid(grid, row, col, num):
    # Check row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

# Backtracking function
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Empty cell
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num  # Assign number
                        if solve_sudoku(grid):  # Recursive call
                            return True
                        grid[row][col] = 0  # Undo assignment (backtrack)
                return False
    return True

# Example Sudoku puzzle (0 = empty)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("=== Original Sudoku Puzzle ===")
print_grid(sudoku_grid)

if solve_sudoku(sudoku_grid):
    print("\n=== Solved Sudoku Puzzle ===")
    print_grid(sudoku_grid)
else:
    print("\nNo solution exists.")
