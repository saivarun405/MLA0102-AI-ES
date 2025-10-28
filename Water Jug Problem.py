from collections import deque
def water_jug_problem():
    jug4 = 4
    jug3 = 3
    initial_state = (0, 0)

    queue = deque([initial_state])
    
    visited = set()
    visited.add(initial_state)

    
    parent = {initial_state: None}
    while queue:
        current = queue.popleft()
        a, b = current
        if a == 2:
            
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        next_states = set()

        next_states.add((jug4, b))
       
        next_states.add((a, jug3))
       
        next_states.add((0, b))
        
        next_states.add((a, 0))
        
        pour = min(a, jug3 - b)
        next_states.add((a - pour, b + pour))
       
        pour = min(b, jug4 - a)
        next_states.add((a + pour, b - pour))

        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                parent[state] = current

solution_path = water_jug_problem()
print("Step-by-step solution (jug4, jug3):")
for step in solution_path:
    print(step)
