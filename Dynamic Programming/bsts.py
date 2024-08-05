

def bsts(length):
    f = [1, 1, 2]
    # for i in range(3, length+1):
    #     f.append(0)
    #     for j in range(i-1, i//2, -1):
    #         f[i] += f[j]

    #     f[i] = 2 * f[i]
        
    #     if i % 2 == 1:
    #         f[i] += f[i//2]

    # f = [0, 1, 2]

    for i in range(3, length+1):
        f.append(0)

        head = 1
        for j in range(1, i//2 + 1):
            f[i] += 2 * (f[head - 1] * f[i - head])
            head += 1

        if i % 2 == 1:
            f[i] += f[head - 1] * f[i - head]

    # print(f)
    return f[length]
 
print(bsts(2))
print(bsts(3))
print(bsts(5))