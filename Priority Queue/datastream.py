import heapq
from itertools import islice

def ksmallest(k, arr):
    smallest = [-x for x in islice(arr, k)]

    heapq.heapify(smallest)

    for element in arr:
        if element < -(smallest[0]):
            heapq.heapreplace(smallest, -element)

    smallest = [-x for x in smallest]

    return smallest


print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
print(ksmallest(3, range(1000000, 0, -1)))
print(ksmallest(5, (x**2 for x in range(10,0,-1))))