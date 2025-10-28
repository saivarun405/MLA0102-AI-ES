puzzle = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def print_puzzle(p):
    for row in p:
        print(row)
    print()

def move(p, direction):
   
    for i in range(3):
        for j in range(3):
            if p[i][j] == 0:
                x, y = i, j
  
    if direction == 'down' and x < 2:
        p[x][y], p[x+1][y] = p[x+1][y], p[x][y]
    elif direction == 'right' and y < 2:
        p[x][y], p[x][y+1] = p[x][y+1], p[x][y]
    else:
        print("Invalid move!")

print("Initial puzzle:")
print_puzzle(puzzle)
move(puzzle, 'down')
print("After step 1 (move down):")
print_puzzle(puzzle)
move(puzzle, 'right')
print("After step 2 (move right):")
print_puzzle(puzzle)
if puzzle == goal:
    print("🎉 Puzzle solved in 2 steps!")
else:
    print("Not solved yet!")