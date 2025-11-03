import numpy as np
import random

# Grid size
ROWS, COLS = 5, 5

# Rewards
GOAL = (4, 4)
OBSTACLES = [(1, 1), (2, 3)]
REWARD_GOAL = 10
REWARD_OBSTACLE = -10
REWARD_STEP = -1

# Q-Learning parameters
alpha = 0.7       # Learning rate
gamma = 0.8       # Discount factor
epsilon = 0.2     # Exploration rate
episodes = 500

# Actions: up, down, left, right
actions = ['up', 'down', 'left', 'right']
Q = np.zeros((ROWS, COLS, len(actions)))

# Check if a position is valid
def is_valid(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS and (x, y) not in OBSTACLES

# Get next state and reward
def step(state, action):
    x, y = state
    if action == 'up':
        x -= 1
    elif action == 'down':
        x += 1
    elif action == 'left':
        y -= 1
    elif action == 'right':
        y += 1
    
    if not is_valid(x, y):
        return state, REWARD_OBSTACLE
    
    if (x, y) == GOAL:
        return (x, y), REWARD_GOAL
    
    return (x, y), REWARD_STEP

# Training using Q-Learning
for ep in range(episodes):
    state = (0, 0)
    while state != GOAL:
        # Choose action (ε-greedy)
        if random.uniform(0, 1) < epsilon:
            action_idx = random.randint(0, len(actions) - 1)
        else:
            action_idx = np.argmax(Q[state[0], state[1]])

        action = actions[action_idx]
        next_state, reward = step(state, action)
        
        # Q-value update
        best_next = np.max(Q[next_state[0], next_state[1]])
        Q[state[0], state[1], action_idx] += alpha * (reward + gamma * best_next - Q[state[0], state[1], action_idx])
        
        state = next_state

print("Learned Q-Table:")
print(np.round(Q, 2))

# Extract optimal path
def get_optimal_path(start):
    path = [start]
    state = start
    while state != GOAL:
        action_idx = np.argmax(Q[state[0], state[1]])
        action = actions[action_idx]
        next_state, _ = step(state, action)
        if next_state == state:  # stuck
            break
        path.append(next_state)
        state = next_state
    return path

optimal_path = get_optimal_path((0, 0))
print("\nOptimal Path from Start to Goal:")
print(optimal_path)

