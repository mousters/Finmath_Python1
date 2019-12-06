def calculate(num1,num2,func):
    fun=func
    return fun(num1,num2)
def divide(num1,num2):
    ans=0
    try:
        ans=num1/num2
    except ZeroDivisionError as error:
        print(error)
    return ans
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
if __name__=='__main__':
    print(calculate(5,123,multiply))
    calculate(5,0,divide)
    # 615
    # division by zero
