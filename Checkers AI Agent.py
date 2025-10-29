import math
import random

# Initialize 8x8 checkers board
def create_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 != 0:
                if i < 3:
                    board[i][j] = 'b'  # Black pieces
                elif i > 4:
                    board[i][j] = 'r'  # Red pieces
    return board

# Display board
def print_board(board):
    print("\n  0 1 2 3 4 5 6 7")
    for i in range(8):
        print(i, end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print()
    print()

# Evaluate board score
def evaluate(board):
    red_score = sum(row.count('r') for row in board)
    black_score = sum(row.count('b') for row in board)
    return red_score - black_score

# Get all possible moves for a player
def get_moves(board, player):
    moves = []
    direction = -1 if player == 'r' else 1
    for i in range(8):
        for j in range(8):
            if board[i][j] == player:
                for dx in [-1, 1]:
                    x, y = i + direction, j + dx
                    if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == ' ':
                        moves.append(((i, j), (x, y)))
    return moves

# Apply move to board
def make_move(board, move):
    new_board = [row[:] for row in board]
    (x1, y1), (x2, y2) = move
    new_board[x2][y2] = new_board[x1][y1]
    new_board[x1][y1] = ' '
    return new_board

# Minimax with Alpha–Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0:
        return evaluate(board), board

    player = 'r' if maximizing_player else 'b'
    moves = get_moves(board, player)

    if not moves:
        return evaluate(board), board

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for move in moves:
            eval_score, _ = minimax(make_move(board, move), depth - 1, alpha, beta, False)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, make_move(board, best_move)
    else:
        min_eval = math.inf
        best_move = None
        for move in moves:
            eval_score, _ = minimax(make_move(board, move), depth - 1, alpha, beta, True)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, make_move(board, best_move)

# Game loop
def play_game():
    board = create_board()
    print_board(board)
    turn = 'r'  # Red (Human)
    
    while True:
        moves = get_moves(board, turn)
        if not moves:
            print("No moves available!")
            winner = 'Black' if turn == 'r' else 'Red'
            print(f"\n🏆 Winner: {winner}")
            break

        print(f"Turn: {'Red (You)' if turn == 'r' else 'Black (AI)'}")

        if turn == 'r':
            # Human move
            print("Available moves:", moves)
            move = random.choice(moves)  # Simple random move (for simplicity)
        else:
            # AI move
            print("AI thinking...")
            _, new_board = minimax(board, 3, -math.inf, math.inf, False)
            board = new_board
            print_board(board)
            turn = 'r'
            continue

        board = make_move(board, move)
        print_board(board)
        turn = 'b' if turn == 'r' else 'r'

# Run the game
play_game()
