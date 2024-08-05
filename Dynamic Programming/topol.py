from collections import defaultdict
import queue

path = []
visited = set()

def order(n, edges):
    adjset = defaultdict(set)
    indegree = [0] * n 
    
    global path, visited
    path, visited, que = [], [0] * n, queue.Queue() 

    for u, v in edges:
        adjset[u].add(v)
        indegree[v] += 1

    for i in range(n):
        if indegree[i] == 0:
            que.put(i)

    # print(f"indegree: {indegree}")

    while not que.empty():
        u = que.get()
        path.append(u)
        for v in adjset[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                que.put(v)

    if path != [] and len(path) == n: 
        return path 
    else: 
        return "None"


def _dfs(adjset, node=0):
    visited[node] = 1

    for v in adjset[node]:
        if visited[v] == 1: # v is still in stack -> cycle found
            return 0
        if visited[v] == 0: # v is not visited
            if _dfs(adjset, v) == 0:
                return 0
    
    visited[node] = 2
    path.append(node)
    return 1


def order2(n, edges):
    adjset = defaultdict(set)
    for u, v in edges:
        adjset[u].add(v)

    global path, visited
    path, visited = [], [0] * n

    for node in range(n):
        if visited[node] == 0:
            if _dfs(adjset, node) == 0:
                return "None"
            
    if path != []: 
        return path[::-1]
    else: 
        return "None"



print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(order(6, [(0,2), (0,1), (2,3), (1,3), (3,4), (3,5)]))
print(order(4, [(0,1), (1,2), (2,1), (2,3)]))
print(order(5, []))
print(order(3, [(1,2), (2,1)]))
print(order(1, [(0,0)]))

print(order2(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(order2(6, [(0,2), (0,1), (2,3), (1,3), (3,4), (3,5)]))
print(order2(4, [(0,1), (1,2), (2,1), (2,3)]))
print(order2(5, []))
print(order2(3, [(1,2), (2,1)]))
print(order2(1, [(0,0)]))




