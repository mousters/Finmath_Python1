# reduce () function receives two arguments:
# a function
# an iterable
# The argument function is applied cumulatively to arguments in the list
# from left to right
# The result of the function in the first call becomes the first argument
# and the third item in list becomes second. This is repeated until the
# list is exhausted.
#CONNECT WITH FOLLOWING EXAMPLE:
#THE FIRST ITEM ON THE LEFT IS 1 AND THE FIRST 'RIGHT' ITEM IS 2 1*2=2
# THE RESULT OF THE FUNC IN THE FIRST CALL BECOMES THE FIRST ARGUMENT -->2
# THE THIRD ITEM BECOMES THE SECOND-->3
# THE RESULT = 2*3 =6
#REPEAT

import functools
def mult(x,y):
    return x*y
if __name__=='__main__':
    factorial=functools.reduce(mult,range(1,6))
    print(factorial)
    #120
