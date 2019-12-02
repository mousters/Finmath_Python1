def decorator_1(function):
    def wrapper():
        print("Something is happening before the function is called")
        a=function()
        print("Something is happening after the function is called")
        return a
    return wrapper
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


