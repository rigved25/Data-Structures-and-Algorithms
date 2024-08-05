w_v = []
memo = {}

# take any item from ith pos, any number of times to get at max W weight
# return the max value gathered

def f(i, W, memo):
    global w_v
    
    if W == 0 or i == len(w_v):
        return 0, [0] * len(w_v)
    
    if i not in memo:
        memo[i] = {}
        
    if W in memo[i]:
        return memo[i][W]
    
    max_val = 0
    max_count = [0] * len(w_v)
    for j in range(i, len(w_v)):
        if W - w_v[j][0] >= 0:
            child, count = f(j, W - w_v[j][0], memo)
            if max_val < child + w_v[j][1]:
                max_val = child + w_v[j][1]
                max_count = count.copy()
                max_count[j] += 1
    
    memo[i][W] = (max_val, max_count)
    return max_val, max_count

def best(W, weights_values):
    global w_v
    w_v = weights_values
    memo = {}
    return f(0, W, memo)

print(best(3, [(1, 5), (1, 5)]))
print(best(58, [(5, 9), (9, 18), (6, 12)]))
print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
