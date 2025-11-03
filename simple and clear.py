# --- ontology_parser.py ---
# Program to parse ontology triples and query subclass relationships

# Step 1: Define ontology triples (Subject, Predicate, Object)
triples = [
    ("Dog", "subClassOf", "Animal"),
    ("Cat", "subClassOf", "Animal"),
    ("Animal", "subClassOf", "LivingBeing"),
    ("Bird", "subClassOf", "Animal"),
    ("Parrot", "subClassOf", "Bird")
]

# Step 2: Build knowledge graph (dictionary-based)
knowledge_graph = {}
for subject, predicate, obj in triples:
    if predicate == "subClassOf":
        if obj not in knowledge_graph:
            knowledge_graph[obj] = []
        knowledge_graph[obj].append(subject)

# Step 3: Find all subclasses of a given class
def find_subclasses(cls):
    subclasses = []

    def dfs(node):
        if node in knowledge_graph:
            for child in knowledge_graph[node]:
                subclasses.append(child)
                dfs(child)

    dfs(cls)
    return subclasses

# Step 4: Check if one class is a subclass of another (directly or indirectly)
def is_subclass(sub, sup):
    return sub in find_subclasses(sup)

# Step 5: Display the ontology graph
print("📘 Knowledge Graph (Ontology Relationships):")
for key, values in knowledge_graph.items():
    print(f"{key} → {values}")

# Step 6: Example Queries
print("\n🔍 Query Results:")

cls = "Animal"
print(f"All subclasses of '{cls}': {find_subclasses(cls)}")

sub, sup = "Parrot", "LivingBeing"
print(f"Is '{sub}' a subclass of '{sup}'? {is_subclass(sub, sup)}")

sub, sup = "Cat", "Bird"
print(f"Is '{sub}' a subclass of '{sup}'? {is_subclass(sub, sup)}")
