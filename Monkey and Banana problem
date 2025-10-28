class State:
    def __init__(self, monkey, box, banana, has_banana=False):
        self.monkey = monkey      # monkey position
        self.box = box            # box position
        self.banana = banana      # banana position
        self.has_banana = has_banana  # goal state

    def __str__(self):
        return f"Monkey: {self.monkey}, Box: {self.box}, Banana: {self.banana}, Has Banana: {self.has_banana}"

def monkey_and_banana():
    # Initial state
    state = State(monkey='A', box='B', banana='C')

    print("Initial State →", state)
    print("\n--- Monkey starts thinking ---")

    # Step 1: Move monkey to box
    if state.monkey != state.box:
        print(f"Monkey moves from {state.monkey} to {state.box}")
        state.monkey = state.box

    # Step 2: Push box to banana
    if state.box != state.banana:
        print(f"Monkey pushes the box from {state.box} to {state.banana}")
        state.box = state.banana
        state.monkey = state.banana

    # Step 3: Climb the box
    print("Monkey climbs onto the box.")

    # Step 4: Grab the banana
    state.has_banana = True
    print("Monkey grabs the banana! 🍌")

    print("\nFinal State →", state)

# Run the simulation
monkey_and_banana()
