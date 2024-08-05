def mergesorted_inversions(a, b, prev_inversions):
    i=0
    j=0
    inversions = 0
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
                inversions += (len(a) - i)
                j += 1
    # print(f"inversions: {inversions}")
    return answer, inversions + prev_inversions  


def _mergesort_inversions(a, i, j):

    # print(f"a:{a}, i:{i}, j:{j}, a[i:j]:{a[i:j+1]}")

    if j-i < 1:
        return a[i:j+1], 0
    mid = (i+j)//2
    left, lft_inversions = _mergesort_inversions(a, i, mid)
    right, rgt_inversions = _mergesort_inversions(a, mid+1, j)
    # print(f"lft_inversions:{lft_inversions}  rgt_inversions:{rgt_inversions}")
    return mergesorted_inversions(left, right, lft_inversions + rgt_inversions)

def num_inversions(a):
    tree, inversions = _mergesort_inversions(a, 0, len(a) - 1)
    print(inversions)
    return inversions

num_inversions([4, 1, 3, 2])
num_inversions([2, 4, 1, 3])