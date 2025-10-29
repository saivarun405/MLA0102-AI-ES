import random

# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print("\n")
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print("\n")

# Function to check for winner
def check_winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False

# Check for draw
def is_draw(b):
    return ' ' not in b

# Player move
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == ' ':
            board[int(move)-1] = 'X'
            break
        else:
            print("Invalid move! Try again.")

# Computer move
def computer_move():
    empty_cells = [i for i in range(9) if board[i] == ' ']
    move = random.choice(empty_cells)
    board[move] = 'O'
    print("Computer chose:", move+1)

# Main game
def play_game():
    print("Welcome to Tic Tac Toe! You are X, Computer is O.")
    print_board()

    while True:
        # Player's move
        player_move()
        print_board()
        if check_winner(board, 'X'):
            print("🎉 You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # Computer's move
        computer_move()
        print_board()
        if check_winner(board, 'O'):
            print("🤖 Computer wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Run the game
play_game()
