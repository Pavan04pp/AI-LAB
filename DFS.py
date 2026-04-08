def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)


# --- User Input Section ---
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")

visited = set()
print("DFS Traversal:")
dfs(graph, start, visited)

