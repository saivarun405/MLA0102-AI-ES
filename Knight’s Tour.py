N = 8  
moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
moves_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Function to print the chessboard
def print_solution(board):
    for row in board:
        print(" ".join(str(x).zfill(2) for x in row))
    print()

# Check if position is valid
def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# Recursive utility function for Knight's Tour
def solve_knight_tour(x, y, move_i, board):
    if move_i == N * N:
        return True

    for k in range(8):
        next_x = x + moves_x[k]
        next_y = y + moves_y[k]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = move_i
            if solve_knight_tour(next_x, next_y, move_i + 1, board):
                return True
            # Backtracking
            board[next_x][next_y] = -1
    return False

# Main function
def knight_tour():
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[0][0] = 0  # Starting position

    if not solve_knight_tour(0, 0, 1, board):
        print("❌ Solution does not exist.")
    else:
        print("✅ Knight’s Tour solution found:\n")
        print_solution(board)

# Run the program
knight_tour()

