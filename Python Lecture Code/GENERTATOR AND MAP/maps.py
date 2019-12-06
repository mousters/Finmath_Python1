# The map() function calls the specified function for each item of an
# iterable (such as string, list,
# tuple or dictionary) and returns a list of results.

import math
def sqrt(x):
    return math.sqrt(x)
if __name__=='__main__':
    sqrList = map (lambda x: x*x, [1, 2, 3,4])
    while True:
        try:
            print(next(sqrList))
        except StopIteration:
            break
    # 1
    # 4
    # 9
    # 16
    sqrtList=map(sqrt,[1,4,9,16,25])
    while True:
        try:
            print(next(sqrtList))
        except StopIteration:
            break
    # 1.0
    # 2.0
    # 3.0
    # 4.0
    # 5.0