from collections import defaultdict
from random import randint
from heapq import heapify, heappop, heappush

memo = defaultdict(tuple)

def is_base_pair_formed(base1, base2):
    pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C'), ('U', 'G'), ('G', 'U')}
    return (base1, base2) in pairs
    
def qselect(k, arr):
    if arr == [] or k < 1 or k > len(arr):
        return None
    else:
        pindex = randint(0, len(arr)-1)
        arr[0], arr[pindex] = arr[pindex], arr[0]
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            qselect(k, left) if k <= lleft else \
            qselect(k-lleft-1, right)
    
def init_memo(rna):
    memo.clear()
    for i in range(0, len(rna)):
        memo[i,i] = (0, -2)
        memo[i,i-1] = (0, -2)

def init_memo_total(rna):
    memo.clear()
    for i in range(0, len(rna)):
        memo[i,i] = 1
        memo[i,i-1] = 1

def init_memo_kbest(rna):
    memo.clear()
    for i in range(0, len(rna)):
        memo[i,i] = [(0, -2, 0, 0)]
        memo[i,i-1] = [(0, -2, 0, 0)]

def print_memo(rna):
    n = len(rna)
    # print("Memoization Table (Format: (Score, Split Point)):\n")
    for i in range(n):
        for j in range(n):
            if (i, j) in memo:
                print(f"{memo[(i, j)][0]}", sep="/t", end=" ")
            else:
                print("0", sep="/t", end=" ")
        print()  # Newline for the next row

def cky_top(rna, i, j):
    # print(f"i,j : {i}, {j}")

    if (i,j) in memo:
        return memo[i,j][0]
    
    # print(f"not in memo i,j : {i}, {j}")

    ans = (-float('inf'), -float('inf'))
    if is_base_pair_formed(rna[i], rna[j]):
        ans = (cky_top(rna, i+1, j-1) + 1, -1)

    for k in range(i, j):
        temp = cky_top(rna, i, k) + cky_top(rna, k+1, j)
        if ans[0] < temp:
            ans = (temp, k)

    memo[i,j] = ans
    return memo[i,j][0]

def cky_bottom(rna):
    n = len(rna)
    init_memo(rna)

    for span in range(2,n+1):
        for i in range(n-span+1):
            j = i + span - 1

            # print(f"i,j : {i}, {j}")

            ans = (-float('inf'), -float('inf'))
            if is_base_pair_formed(rna[i], rna[j]):
                ans = (memo[i+1, j-1][0] + 1, -1)

            for k in range(i, j-1):
                if ans[0] < memo[i, k][0] + memo[k+1, j][0]:
                    ans = (memo[i, k][0] + memo[k+1, j][0], k)
            
            memo[i,j] = ans

def cky_back(path, i, j):
    if memo[i, j] == (0, -2):
        return path

    if memo[i, j][1] == -1:
        path[i] = '('
        path[j] = ')'
        return cky_back(path, i+1, j-1)
    elif memo[(i, j)][1] >= 0:
        k = memo[(i, j)][1]
        path = cky_back(path, i, k)
        path = cky_back(path, k+1,j)
        return path


def nussinov_top(rna, i, j):
    if (i, j) in memo:
        return memo[i, j]

    ans = (nussinov_top(rna, i, j-1)[0], -1)

    for k in range(i, j):
        if is_base_pair_formed(rna[j], rna[k]):
            temp = (nussinov_top(rna, i, k-1)[0] + nussinov_top(rna, k+1, j-1)[0] + 1, k)
            # print(f"ans:{ans} temp:{temp}")
            if ans[0] < temp[0]:
                ans = temp

    memo[i, j] = ans
    return memo[i, j]

def nussinov_bottom(rna):
    n = len(rna)
    init_memo(rna)

    for span in range(2,n+1):
        for i in range(n-span+1):
            j = i + span - 1

            # print(f"i,j : {i}, {j}")

            ans = (memo[i, j-1][0], -1)
                
            for k in range(i, j):
                if is_base_pair_formed(rna[k], rna[j]):
                    if ans[0] < memo[i, k-1][0] + memo[k+1, j-1][0] + 1:
                        ans = (memo[i, k-1][0] + memo[k+1, j-1][0] + 1, k)
            
            memo[i,j] = ans

def nussinov_back(path, i, j):
    # print(f" i:{i} j:`{j} memo[i,j]: {memo[i, j]} path:{''.join(path)}")
    if memo[i, j] == (0, -2):
        return path

    if memo[i, j][1] == -1:
        return nussinov_back(path, i, j-1)
    elif memo[(i, j)][1] >= 0:
        k = memo[(i, j)][1]
        path = nussinov_back(path, i, k-1)

        path[k] = '('
        path[j] = ')'

        path = nussinov_back(path, k+1, j-1)
        return path


def best(rna):
    n = len(rna)
    i, j = 0, n-1

    # # CKY top-down
    # init_memo(rna)
    # cky_top(rna, i, j)

    # pairs = memo[i,j][0]

    # path = ['.'] * n
    # path = cky_back(path, i, j)

    # # CKY bottom-up
    # cky_bottom(rna)

    # pairs = memo[i,j][0]

    # path = ['.'] * n
    # path = cky_back(path, i, j)

    # # nussinov top-down
    # init_memo(rna)
    # nussinov_top(rna, i, j)

    # pairs = memo[i,j][0]

    # path = ['.'] * n
    # path = nussinov_back(path, i, j)

    # nussinov bottom-up
    nussinov_bottom(rna)

    pairs = memo[i,j][0]

    path = ['.'] * n
    path = nussinov_back(path, i, j)

    print_memo(rna)

    return pairs, "".join(path)

def total(rna):
    n = len(rna)
    init_memo_total(rna)

    for span in range(2,n+1):
        for i in range(n-span+1):
            j = i + span - 1

            ans = memo[i, j-1]
                
            for k in range(i, j):
                if is_base_pair_formed(rna[k], rna[j]):
                        ans = ans + (memo[i, k-1] * memo[k+1, j-1])
            
            memo[i,j] = ans
        
    return memo[0, n-1]

def nussinov(rna, K):
    n = len(rna)
    init_memo_kbest(rna)

    for span in range(2,n+1):
        for i in range(n-span+1):
            j = i + span - 1

            # print(f"i,j : {i}, {j}")

            # make the list of tuples which will be sent to the nbest.
            ABs = []
            ABs.append((-1, (i, j-1), ()))
            
            for k in range(i, j):
                if is_base_pair_formed(rna[k], rna[j]):
                    ABs.append((k, (i, k-1), (k+1, j-1)))
            
            ans = nbest(ABs, K)

            memo[i,j] = ans

def nbest(ABs, n):
    def trypush(k, A, B, i, j):
        if i<len(memo[A]) and j<len(memo[B]) and (id(A), id(B), k, i, j) not in used:
            heappush(h, (memo[A][i][0] + memo[B][j][0] - 1, k, A, B, i, j))
            used.add((id(A), id(B), k, i, j))

    def trypushB(k, A, B, i, j):
        if i<len(memo[A]) and (id(A), id(B), k, i, j) not in used:
            heappush(h, (memo[A][i][0], k, A, B, i, j))
            used.add((id(A), id(B), k, i, j))

    h, used, result = [], set(), []

    for (k, A, B) in ABs:
        if k >= 0:     # binary case
            h.append((memo[A][0][0] + memo[B][0][0] - 1, k, A, B, 0, 0))
        elif k == -1:   #unary case
            h.append((memo[A][0][0], k, A, B, 0, 0))

    heapify(h)

    # print(f"intial heap: {h}")

    while h and n:
        n = n-1
        (pairs, k, A, B, i, j) = heappop(h)
        # print(f"(pairs, k, A, B, i, j): {(pairs, k, A, B, i, j)}")

        result.append((pairs, k, i, j))

        if k >= 0:     # binary case
            trypush(k, A, B, i+1, j)
            trypush(k, A, B, i, j+1)
        elif k == -1:   #unary case
            trypushB(k, A, B, i+1, j)
        
    return result

def nussinov_kbest_back(path, k, i, j, p, q):
    # print(f" i:{i} j:`{j} memo[i,j]: {memo[i, j]} path:{''.join(path)}")
    if k == -2:
        return path

    if k == -1:
        A = i, j-1
        (pairs, X, p_child, q_child) = memo[A][p]
        return nussinov_kbest_back(path, X, i, j-1, p_child, q_child)
    elif k >= 0:
        A = i, k-1
        B = k+1, j-1

        (pairs, X, p_child, q_child) = memo[A][p]
        path = nussinov_kbest_back(path, X, i, k-1, p_child, q_child)

        path[k] = '('
        path[j] = ')'

        (pairs, X, p_child, q_child) = memo[B][q]
        path = nussinov_kbest_back(path, X, k+1, j-1, p_child, q_child)
        return path


def kbest(rna, K):
    n = len(rna)
    i, j = 0, n-1

    nussinov(rna, K)

    # for x in memo[i,j]:
    #     print(x)

    result = []
    for (pairs, k, p, q) in memo[i, j]:
        path = ['.'] * n
        nussinov_kbest_back(path, k, i, j, p, q)
        result.append((-pairs, "".join(path)))

    return result

# print(best("GCACG"))
# print(best("UUCAGGA"))
# print(best("GUUAGAGUCU"))
# print(best("AUAACCUUAUAGGGCUCUG"))
# print(best("AGGCAUCAAACCCUGCAUGGGAGCG"))
# print(best("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU"))
# print(best("GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG"))
# print(best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU"))
# print(best("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC"))
# print(best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA"))

# print(total("ACAGU"))
# print(total("UUUGGCACUA"))
# print(total("GAUGCCGUGUAGUCCAAAGACUUC"))
# print(total("AGGCAUCAAACCCUGCAUGGGAGCG"))

print(kbest("ACAGU", 3))
print(kbest("AGGCAUCAAACCCUGCAUGGGAGCG", 10))
