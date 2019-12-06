def isPresent (root,val):
    # write your code here
    # return 1 or 0 depending on whether the element is present in the tree or not
    cur = root
    while cur:
        if cur.value == val:
            return 1
        elif cur.value < val:
            cur = cur.right
        else:
            cur = cur.left
    return 0