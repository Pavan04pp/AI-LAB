def dls(tree, node, limit, visited=None):
    if visited is None:
        visited = set()
    
    # Visit node
    print(node, end=" ")
    visited.add(node)
    
    # If depth limit reached, stop
    if limit == 0:
        return
    
    # Recur for neighbors
    for neighbor in tree[node]:
        if neighbor not in visited:
            dls(tree, neighbor, limit - 1, visited)


# Example tree (adjacency list)
tree = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6','7'],
    '4': [],
    '5': [],
    '6': [],
    '7':[]
}

print("DLS Traversal (limit = 2):", end=" ")
dls(tree, '1', 2)
