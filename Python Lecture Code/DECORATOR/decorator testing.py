from time_decorator import timer
from  upper_case_decorator import decorator_1,uppercase_decorator
from string_splitter import split_string
from counter import call_counter
@timer
def counting(num):
    temp=0
    for i in range(num):
        temp+=i
    return temp

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

@call_counter
def succ(x):
    return x + 1


if __name__ == '__main__':
    # print('time decorator')
    counting(1)
    counting(10000000)
    # print('upper case decorator')
    decorate = uppercase_decorator(say_hi)
    print(decorate())
    print (say_bye())
    say_name()
    # print('split decorator')
    print(welcome())

    # print('counting decorator')
    print(succ.calls)
    for i in range(10):
        print('function output : {0}'.format(succ(i)))
    print('calls after execution: {0}'.format(succ.calls))


#OUTPUT
# decorator called
# time decorator
# Finished 'counting' in 0.0000 secs
# Finished 'counting' in 0.8623 secs

# upper case decorator
# HELLO
# Something is happening before the function is called
# Something is happening after the function is called
# BYE, SEE YOU TOMORROW
# Something is happening before the function is called
# James
# Something is happening after the function is called


# split decorator
# ['WELCOME', 'TO', 'OUR', 'PARTY', 'AMIGOS']


# counting decorator
# 0
# decorator called :1
# function output : 1
# decorator called :2
# function output : 2
# decorator called :3
# function output : 3
# decorator called :4
# function output : 4
# decorator called :5
# function output : 5
# decorator called :6
# function output : 6
# decorator called :7
# function output : 7
# decorator called :8
# function output : 8
# decorator called :9
# function output : 9
# decorator called :10
# function output : 10
# calls after execution: 10