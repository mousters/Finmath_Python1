#generator
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        print (func.__name__ + str(Fibonacci(helper.calls)))
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__
    return helper

@call_counter
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__=='__main__':
    print(Fibonacci(10))
    iter=fib(10)

    for i in range(10):
        iter.__next__()
