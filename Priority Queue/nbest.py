from itertools import product
import random
import heapq

def qselect(target_index, a):

    if a == []:
        return []
    
    # select pivot randomized
    pivot_index = random.randint(0, len(a) - 1)
    (pivot_a, pivot_b) = a[pivot_index]
    
    left = []
    right = []
    
    for i, (_a, _b) in enumerate(a):
        if i != pivot_index:
            if _a + _b > pivot_a + pivot_b or (_a + _b == pivot_a + pivot_b and _b > pivot_b):
                right.append((_a, _b))
            else:
                left.append((_a, _b))

    # print(f"a:{a}, pivot: {pivot}, target_index: {target_index}, len(left): {len(left)}, left: {left}")

    if target_index == len(left) + 1:
        # print("FOUND IT")
        return (pivot_a, pivot_b)
    elif target_index < len(left) + 1:
        # print("Checking the left subtree...")
        return qselect(target_index, left)
    else:
        # print("Checking the right subtree...")
        return qselect(target_index - len(left) - 1, right)

def custom_sort_key(tuple):
    return tuple[0] + tuple[1], tuple[1]

def nbesta(arr1, arr2):
    n = len(arr1)

    cartesian_product = list(product(arr1, arr2))

    sorted_list = sorted(cartesian_product, key=custom_sort_key)

    return sorted_list[:n]

def nbestb(arr1, arr2):
    n = len(arr1)

    # arr1.sort()
    arr2.sort()
    
    cartesian_product = list(product(arr1, arr2))

    pivot = qselect(n+1, cartesian_product)

    sorted_list = []
    for tuple in cartesian_product:
        if tuple[0] + tuple[1] < pivot[0] + pivot[1]:
            sorted_list.append(tuple)
        elif tuple[0] + tuple[1] == pivot[0] + pivot[1] and tuple[1] < pivot[1]:
            sorted_list.append(tuple)
    
    sorted_list = sorted(sorted_list, key=custom_sort_key)
    return sorted_list

def nbestc(a, b):
    n = len(a)

    a.sort()
    b.sort()

    visited = set()

    sorted_list = []
    heap = [(a[0] + b[0], b[0], (0, 0))]

    while len(sorted_list) < n:
        # pop the top into the sorted_list
        (sum, y, (i, j)) = heapq.heappop(heap)
        sorted_list.append((a[i], b[j]))

        # push its children
        if (a[i+1] + b[j], b[j], (i+1, j)) not in visited:
            # print(f"Pushing: {(a[i+1] + b[j], b[j], (i+1, j))}")
            heapq.heappush(heap, (a[i+1] + b[j], b[j], (i+1, j)))
            visited.add((a[i+1] + b[j], b[j], (i+1, j)))
        
        if (a[i] + b[j+1], b[j+1], (i, j+1)) not in visited:
            # print(f"Pushing: {(a[i] + b[j+1], b[j+1], (i, j+1))}")
            heapq.heappush(heap, (a[i] + b[j+1], b[j+1], (i, j+1)))
            visited.add((a[i] + b[j+1], b[j+1], (i, j+1)))

    return sorted_list


a, b = [4, 1, 5, 3], [2, 6, 3, 4]            
print(nbesta(a, b))
print(nbestb(a, b))
print(nbestc(a, b))