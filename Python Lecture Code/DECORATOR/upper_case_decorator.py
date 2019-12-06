from string_splitter import split_string
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

@decorator_1
@uppercase_decorator
def say_bye():
    return 'bye, see you tomorrow'
# Something is happening before the function is called
# Something is happening after the function is called
# BYE
#note both decorators are called

@decorator_1
def say_name():
    print('James')

def say_hi():
    return 'hello'

@split_string
@uppercase_decorator
def welcome():
    return 'welcome to our party amigos'

if __name__ == '__main__':

# print('upper case decorator')
    decorate = uppercase_decorator(say_hi)
    print(decorate())
    print (say_bye())
    say_name()
    print('split decorator')
    print(welcome())
