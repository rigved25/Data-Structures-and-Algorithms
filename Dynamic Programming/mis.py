
# top-down
def _max_wis(dp, i):
    if i < 0:
        return 0, []

    max1, lst1 = _max_wis(dp, i-1)
    max2, lst2 = _max_wis(dp, i-2)

    if max2 + dp[i] > max1:
        lst2.append(dp[i]) 
        return max2 + dp[i], lst2
    else:
        return max1, lst1

# bottom-up
def max_wis(a):
    # return _max_wis(a, len(a) - 1)

    dp = [(0, []), (0, [])]
    k = 1
    for i in range(0, len(a)):
        # i-2
        k = (k + 1) % 2
        j = (k + 1) % 2
        if dp[k][0] + a[i] > dp[j][0]:
            dp[k] = (( dp[k][0] + a[i], dp[k][1] + [a[i]] ))
        else:
            dp[k] = (( dp[j][0], dp[j][1] ))

    return dp[k][0], dp[k][1]

print(max_wis([7,8,5]))
print(max_wis([-1,8,10]))
print(max_wis([9,10,8,5,2,4]))
print(max_wis([]))
