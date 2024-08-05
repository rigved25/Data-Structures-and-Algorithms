def sort(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]

def sorted(tree):
    answer = []
    _sorted(tree, answer)
    return answer

def _sorted(tree, answer):
    if tree == []:
        return
    left, root, right = tree
    _sorted(left, answer)
    answer.append(root)
    _sorted(right, answer)

def search(tree, x):
    if tree == []:
        return False
    left, root, right = tree
    if root == x:
        return True
    elif root > x:
        return search(left, x)
    else:
        return search(right, x)

def insert(tree, x):
    _insert(tree, x)

def _insert(tree, x):
    if tree == []:
        #insert
        return [[], x, []]
    
    left, root, right = tree

    if root == x:
        return tree
    elif root > x:
        tree[0] = _insert(left, x)
        return tree
    else:
        tree[2] = _insert(right, x)
        return tree
