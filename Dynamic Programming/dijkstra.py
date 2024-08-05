from heapdict import heapdict
from collections import defaultdict

# # wrong because global path will not work
# def shortest(n, edges):
#     adjset = defaultdict(set)

#     # global path, visited
#     path, visited = [], [0] * n

#     for u, v, w in edges:
#         adjset[u].add((v, w))
#         adjset[v].add((u, w))
    
#     heap = heapdict()

#     for node in adjset:
#         heap[node] = float('inf')
    
#     heap[0] = 0

#     while bool(heap):
#         # top node is popped.
#         node, dis = heap.popitem()

#         if dis == float('inf'):
#             break

#         path.append(node)

#         # print(f"node, dis: {node, dis}")

#         if node == n - 1:
#             return dis, path

#         # go thru all its edges and update the heap. 
#         for child, weight in adjset[node]:
#             # print(f"child: {child} weight: {weight}")

#             if child in heap and heap[child] > dis + weight:
#                 heap[child] = dis + weight

#     return None

# little slow because of not using backpointers, and adding elements to the list, and storing all this data
def shortest(n, edges):

    adjset = defaultdict(set)

    for u, v, w in edges:
        adjset[u].add((v, w))
        adjset[v].add((u, w))

    heap = heapdict()

    for node in adjset:
        heap[node] = (float('inf'), [])

    heap[0] = (0, [0])

    while heap:
        node, (dis, path) = heap.popitem()

        if dis == float('inf'):
            break

        # print(f"node, dis, path: {node} {dis} {path}")

        if node == n - 1:
            return dis, path

        for child, weight in adjset[node]:
            # print(f"child: {child} weight: {weight}")

            if child in heap and dis + weight < heap[child][0]:
                heap[child] = (dis + weight, path + [child])
                # print(f"heap[child] after updating: {heap[child]}")
    
    return None

# uses back pointer
def shortest(n, edges):

    adjset = defaultdict(set)

    for u, v, w in edges:
        adjset[u].add((v, w))
        adjset[v].add((u, w))

    heap = heapdict()
    previous = {i: None for i in range(n)}

    for node in adjset:
        heap[node] = float('inf')

    heap[0] = 0

    while heap:
        node, dis = heap.popitem()

        if dis == float('inf'):
            break

        print(f"node, dis: {node, dis}")

        if node == n - 1:
            path = []
            while node is not None:
                path.append(node)
                node = previous[node]
            path.reverse()
            return (dis, path)

        for child, weight in adjset[node]:
            print(f"child: {child} weight: {weight}")

            if child in heap and dis + weight < heap[child]:
                previous[child] = node
                heap[child] = dis + weight
    
    return None



print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
print(shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
print(shortest(4, [(0,1,1), (2,3,1)]))

    