import sys

def count_leaf_nodes(tree, root):
    if root == -1:
        return 0
    
    queue = [root]
    leaf_count = 0
    
    while queue:
        node = queue.pop()
        if not tree[node]:  # 자식이 없다면 리프 노드
            leaf_count += 1
        else:
            queue.extend(tree[node])
    
    return leaf_count

N = int(sys.stdin.readline().strip())
parents = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline().strip())

tree = [[] for _ in range(N)]
root = -1

for child, parent in enumerate(parents):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)

def delete_subtree(node):
    tree[node] = []  # 삭제 노드의 자식 노드 제거
    for parent in range(N):
        if node in tree[parent]:
            tree[parent].remove(node)
    
    for child in range(N):
        if parents[child] == node:
            delete_subtree(child)

delete_subtree(delete_node)

if delete_node == root:
    print(0)
else:
    print(count_leaf_nodes(tree, root))