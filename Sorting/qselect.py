import random

def qselect(target_index, a):

    if a == []:
        return []
    
    # select pivot randomized
    pivot_index = random.randint(0, len(a) - 1)
    pivot = a[pivot_index]
    
    left = []
    right = []
    
    for i, x in enumerate(a):
        if i != pivot_index:
            if x >= pivot:
                right.append(x)
            else:
                left.append(x)

    # print(f"a:{a}, pivot: {pivot}, target_index: {target_index}, len(left): {len(left)}, left: {left}")

    if target_index == len(left) + 1:
        # print("FOUND IT")
        return pivot
    elif target_index < len(left) + 1:
        # print("Checking the left subtree...")
        return qselect(target_index, left)
    else:
        # print("Checking the right subtree...")
        return qselect(target_index - len(left) - 1, right)
