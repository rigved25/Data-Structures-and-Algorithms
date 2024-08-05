from collections import defaultdict
import queue

path = []
visited = set()

def _dfs(adjset, node=0):
    path.append(node)

    for v in adjset[node]:
        if v not in visited:
            visited.add(v)
            _dfs(adjset, v)

def bfs(n, edges):
    adjset = defaultdict(set)   # adjacency set for unweighted
    for u, v in edges: # u->v
        adjset[u].add(v)

    global path, visited
    path, visited, que = [], set(), queue.Queue()        
    
    visited.add(0)
    que.put(0)

    while not que.empty():
        u = que.get()
        path.append(u)

        for v in adjset[u]:
            if v not in visited:
                visited.add(v)
                que.put(v)
        

    
    return path

def dfs(n, edges):
    adjset = defaultdict(set)   # adjacency set for unweighted
    for u, v in edges: # u->v
        adjset[u].add(v)

    global path, visited
    path, visited = [], set()
    _dfs(adjset)
    return path

print(bfs(6, [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5)]))
print(dfs(6, [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5)]))
