import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])


y = np.array([[0],
              [1],
              [1],
              [0]])


W1 = np.random.rand(2, 2)  
W2 = np.random.rand(2, 1)  


hidden_input = np.dot(X, W1)
hidden_output = sigmoid(hidden_input)

final_input = np.dot(hidden_output, W2)
final_output = sigmoid(final_input)

print("Input:")
print(X)
print("\nPredicted Output:")
print(np.round(final_output, 3))
