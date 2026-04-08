def dls(graph, node, depth, visited):
    # Print the current node as we visit it
    print(node, end=" ")
    
    if depth <= 0:
        return

    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dls(graph, neighbor, depth - 1, visited)

def iddfs(graph, start, max_depth):
    for d in range(max_depth + 1):
        print(f"Depth Level {d}:", end=" ")
        # Reset visited for each new depth iteration
        dls(graph, start, d, set())
        print() # New line for the next level

# --- Input Section (Condensed) ---
graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    name = input("Node name: ")
    graph[name] = input(f"Neighbors of {name}: ").split()

start = input("Start node: ")
limit = int(input("Max depth: "))

print("\nIDDFS Traversal:")
iddfs(graph, start, limit)
