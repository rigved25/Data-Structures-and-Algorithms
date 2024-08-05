
    
# def best(W, w_v):
    
#     n = len(w_v)
#     dp = [[0, []] * (W + 1) for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for weight in range(1, W + 1):
#             weight_lim = min(weight // w_v[i - 1][0], w_v[i - 1][2])
#             max_val = 0
#             for k in range(weight_lim + 1):
#                 max_val = max(max_val, dp[i - 1][weight - k * w_v[i - 1][0]] + k * w_v[i - 1][1])
#             dp[i][weight] = max_val

#     return dp[n][W]




def best(W, w_v):
    n = len(w_v)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    def knapsack_bounded(i, weight):
        
        if i == 0 or weight == 0:
            return 0, [0] * n

        if dp[i][weight] != 0:
            return dp[i][weight]

        weight_lim = min(weight // w_v[i - 1][0], w_v[i - 1][2])
        max_val = 0
        item_counts = [0] * n
        for k in range(weight_lim + 1):
                val, cnt = knapsack_bounded(i - 1, weight - (k * w_v[i - 1][0]))

                if val + (k * w_v[i - 1][1]) > max_val:
                    max_val = val + (k * w_v[i - 1][1])
                    item_counts = cnt.copy()
                    item_counts[i - 1] = k

        dp[i][weight] = (max_val, item_counts)
        return dp[i][weight]

    return knapsack_bounded(n, W)



print(best(3, [(2, 4, 2), (3, 5, 3)]))
print(best(3, [(1, 5, 2), (1, 5, 3)]))
print(best(3, [(1, 5, 1), (1, 5, 3)]))
print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
 