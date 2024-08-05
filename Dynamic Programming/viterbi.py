from collections import defaultdict
import queue
from collections import deque


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

    return path, adjset

def longest(n, edges):
    path, adjset = order(n, edges) # path is always present because guaranteed DAG


    longest = [(0, -1) for _ in range(n)] #(longest path till node i, node parent of i which gives longest path)
    max_node = 0
    for node in path:
        for v in adjset[node]:
            if longest[v][0] < longest[node][0] + 1:
                longest[v] = (longest[node][0] + 1, node)

            if longest[v][0] > longest[max_node][0]:
                max_node = v

    path = deque()
    save = max_node
    while max_node != -1:
        path.appendleft(max_node)
        max_node = longest[max_node][1]

    return (longest[save][0], list(path))

print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))


    