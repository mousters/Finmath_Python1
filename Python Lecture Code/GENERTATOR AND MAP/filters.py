# The filter() function calls the specified function which returns
# boolean for each item of the
# specified iterable (list

def isPrime (x):
    check=True
    #NOTE THIS IS BRUTE FORCE WAY WHICH IS MUCH SLOWER AND NOT OPTIMIZED
    for n in range(2,x):
        if x%n ==0:
            check=False
    return check
if __name__=='__main__':
    fltrObj = filter(isPrime, range(100))
    # '''note this object exist only once, if print again, the list(fltrObj) becomes empty'''
    print('Prime numbers between 1 and 10:', list(fltrObj))

# Prime numbers between 1 and 10: [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
