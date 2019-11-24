def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
def say_hi():
    return 'hello'

@uppercase_decorator
def say_bye():
    return 'bye'

if __name__ == '__main__':
    decorate = uppercase_decorator(say_hi)
    print(decorate())
    print (say_bye())