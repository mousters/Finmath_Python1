'''example of divide by zero example'''
def divide(num1,num2):
    ans=0
    try:
        ans=num1/num2
    except ZeroDivisionError as error:
        print(error)
    return ans
def test_except(num1,num2):
    ans=0
    try:
        ans=num1/num2
    except ZeroDivisionError as error:
        print(error)
    else:
        '''this make sure it is always executed'''
        '''this is used to debug, so try is only used to catch errors, but if no error caught, execute code in the else'''
        print('else reached')
        ans=num1+100
    return ans
if __name__ == '__main__':
    test_except(1,0)
    test_except(1,2)