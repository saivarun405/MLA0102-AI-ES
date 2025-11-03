import random
import math

# --- Define the problem ---
tasks = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
time_slots = [1, 2, 3]  # available time slots

# --- Cost function: penalize slot conflicts ---
def cost_function(schedule):
    slot_count = {slot: 0 for slot in time_slots}
    for slot in schedule.values():
        slot_count[slot] += 1
    
    # Penalize overfilled slots (more than 2 tasks per slot)
    cost = 0
    for count in slot_count.values():
        if count > 2:
            cost += (count - 2) * 10  # penalty
    return cost

# --- Generate a random schedule ---
def random_schedule():
    return {task: random.choice(time_slots) for task in tasks}

# --- Generate a neighbor by changing one task’s slot ---
def neighbor(schedule):
    new_schedule = schedule.copy()
    task = random.choice(tasks)
    new_schedule[task] = random.choice(time_slots)
    return new_schedule

# --- Simulated Annealing Algorithm ---
def simulated_annealing(T=100, cooling_rate=0.95, min_T=0.1):
    current = random_schedule()
    best = current
    current_cost = cost_function(current)
    best_cost = current_cost
    
    print("Initial Schedule:", current, " | Cost:", current_cost)
    
    while T > min_T:
        new = neighbor(current)
        new_cost = cost_function(new)
        delta = new_cost - current_cost
        
        # Accept new solution if better or probabilistically if worse
        if delta < 0 or random.random() < math.exp(-delta / T):
            current = new
            current_cost = new_cost
            
            if new_cost < best_cost:
                best = new
                best_cost = new_cost
        
        T *= cooling_rate  # Decrease temperature
    
    return best, best_cost

# --- Run the algorithm ---
best_schedule, best_cost = simulated_annealing()

print("\n✅ Best Schedule Found:", best_schedule)
print("💰 Final Cost:", best_cost)
