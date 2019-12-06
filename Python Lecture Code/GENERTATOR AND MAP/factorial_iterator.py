class iterator_factorial():
    def __init__(self, stop=5):
        self.current = 1
        self.factorial = 1
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        if self.current <= self.stop:
            self.factorial =  self.factorial * self.current
            self.current+=1
            return self.factorial
        else:
            raise StopIteration

if __name__=='__main__':
    iter=iterator_factorial(10)
    for i in range(10):
        print(iter.next())