def find(node):
    if disjoint_set[node] == node:
        return node
    else:
        disjoint_set[node] = find(disjoint_set[node])
        return disjoint_set[node]
    
def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            disjoint_set[root1] = root2
        elif rank[root1] == rank[root2]:
            disjoint_set[root1] = root2
            rank[root2] += 1
        else:
            disjoint_set[root2] = root1
            
disjoint_set = [i for i in range()]
rank = [0 for _ in range()]