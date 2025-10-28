N = 8  
def print_solution(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print("\n")
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, row=0):
    if row == N:
        print_solution(board)
        return True
    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            res = solve_n_queens(board, row + 1) or res
            board[row][col] = 0  # Backtrack
    return res

def eight_queens():
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens(board):
        print("No solution exists")

# Run the program
eight_queens()
