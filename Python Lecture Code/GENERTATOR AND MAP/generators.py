# A generator is a special type of function which does not
# return a single value, instead it returns an iterator object
# with a sequence of values. In a generator function, a yield

def fibonacci(n):
    n_1=1
    n_2=0
    for i in range(n):
        ans=n_1+n_2
        yield ans
        n_2=n_1
        n_1=ans

# another example
def csv_reader (file_name):
    file = open(file_name)
    result =file.read().split("\n")
    return result
def csv_reader (file_name):
    for row in open(file_name , "r"):
        yield row

if __name__=='__main__':
    #first fibonacci
    gen = fibonacci(10)
    while True:
        try:
            print(next(gen))
        except StopIteration:
            print('Fibonacci Stopped')
            break
    # 1
    # 2
    # 3
    # 5
    # 8
    # 13
    # 21
    # 34
    # 55
    # 89
    #second fibonacci
    print([i for i in fibonacci(10)])
    # [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
