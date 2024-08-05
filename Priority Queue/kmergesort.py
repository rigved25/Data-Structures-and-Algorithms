import heapq

def kmergesort(arr, k):
    (top, pq) = _kmergesort(arr, k)
    return pq

def _kmergesort(arr, k):
    n = len(arr)
    
    if n <= k:
        heapq.heapify(arr)
        return (arr[0], arr)
    
    heap = []
    sorted_arr = []
    for i in range(0, n, n//k):
        (top, pq) = _kmergesort(arr[i:i+(n//k)], k)
        heap.append((top, pq))
        
    heapq.heapify(heap)
    
    while heap:
        # send the top into the sorted list
        (top, pq) = heap[0]
        sorted_arr.append(top)
        
        # change the top element of the main heap
        if len(pq) == 1:
            heapq.heappop(heap)
        else:
            # older value is used now get the next in pq
            heapq.heappop(pq)
            heapq.heapreplace(heap, (pq[0], pq))
    
    return (sorted_arr[0], sorted_arr)


print(kmergesort([4,1,5,2,6,3,7,0], 3))