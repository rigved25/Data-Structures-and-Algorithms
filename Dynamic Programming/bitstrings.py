# def num_no(length):
#     return _num_no()

# # ~ O(a^n)
# def _num_no(a, i, length):
#     if len(a) == length or length == 0:
#         return 1
    
#     if len(a) > 0 and a[i-1] == 0:
#         a.append(1)
#         return _num_no(a, i+1, length)
#     else:
#         a.append(1)
#         left = _num_no(a, i+1, length)

#         a.append(0)
#         right = _num_no(a, i+1, length)

#         return left + right

def num_no(length):
    dp = [1, 2]

    for i in range(2, length + 1):
        dp.append(dp[i-1] + dp[i-2])

    return dp[-1]

def num_yes(length):
    dp = [1, 2]
    total = 2
    for i in range(2, length + 1):
        dp.append(dp[i-1] + dp[i-2])
        total = total * 2
    
    return total - dp[-1]

print(num_no(3))
print(num_yes(3))