# Backward Chaining in Python

# Knowledge Base: Horn Clauses (rules and facts)
knowledge_base = [
    (["mammal(A)"], "vertebrate(A)"),
    (["vertebrate(A)"], "animal(A)"),
    (["vertebrate(A)", "flying(A)"], "bird(A)")
]

# Facts
facts = [
    "vertebrate('duck')",
    "flying('duck')",
    "mammal('cat')"
]

# Function to check if a goal can be proven
def backward_chaining(goal):
    print(f"Proving goal: {goal}")
    
    # If the goal is already a known fact
    if goal in facts:
        print(f"✅ {goal} is a known fact.")
        return True

    # Try to find a rule whose conclusion matches the goal
    for premises, conclusion in knowledge_base:
        # Substitute variable A if present
        if conclusion.startswith(goal.split("(")[0]):
            variable = "A"
            if "(" in goal:
                term = goal[goal.find("(")+1 : goal.find(")")]
                # Replace A with the actual term in the premises
                new_premises = [p.replace(variable, term) for p in premises]
            else:
                new_premises = premises

            print(f"Checking rule: {premises} => {conclusion}")
            print(f"Derived sub-goals: {new_premises}")

            # Try to prove all sub-goals recursively
            if all(backward_chaining(sub_goal) for sub_goal in new_premises):
                print(f"✅ {goal} can be derived using {premises} => {conclusion}")
                return True

    print(f"❌ {goal} cannot be proven from the knowledge base.")
    return False


# --- MAIN PROGRAM ---
goal = input("Enter a goal (e.g., animal('cat')): ")

if backward_chaining(goal):
    print(f"\n✅ Conclusion: {goal} can be derived from the knowledge base.")
else:
    print(f"\n❌ Conclusion: {goal} cannot be derived from the knowledge base.")
