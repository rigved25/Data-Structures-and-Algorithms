def mergesorted(a, b):
    i=0
    j=0
    answer = []
    while True:
        if i == len(a):
            answer.extend(b[j:])
            break
        elif j == len(b):
            answer.extend(a[i:])
            break
        else:
            if a[i] <= b[j]:
                answer.append(a[i])
                i += 1
            else:
                answer.append(b[j])
                j += 1

    return answer    


def _mergesort(a, i, j):

    # print(f"a:{a}, i:{i}, j:{j}, a[i:j]:{a[i:j+1]}")

    if j-i < 1:
        return a[i:j+1]
    mid = (i+j)//2
    left = _mergesort(a, i, mid)
    right = _mergesort(a, mid+1, j)
    # print(f"left:{left}  right:{right}")
    return mergesorted(left, right)

def mergesort(a):
    return _mergesort(a, 0, len(a) - 1)

# print(mergesort([4, 2, 5, 1, 6, 3]))
# print(mergesorted([2, 4, 5], [1, 3, 6]))