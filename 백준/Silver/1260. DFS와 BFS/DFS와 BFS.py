def dfs(graph, start, visited):
    visited.add(start)
    dfs_result.append(start)
    
    for neighbor in sorted(graph[start]):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    queue = [start]
    visited = set([start])
    
    while queue:
        node = queue.pop(0)
        bfs_result.append(node)
        
        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs_result = []
bfs_result = []

dfs(graph, V, set())

bfs(graph, V)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
