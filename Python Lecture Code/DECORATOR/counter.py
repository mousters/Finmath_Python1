def call_counter(func):
    def helper(x):
        # print('reach 2nd')
        # '''this is initialize here, throught +=1, but now the helper does not have any value'''
        # '''bc before this code is called, the helper.calls will be intialize to 0 below'''
        helper.calls += 1
        print('decorator called :{0}'.format(helper.calls))
        return func(x)

    # print('reach 1st')
    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1


if __name__ == '__main__':

    print('counting decorator')
    print(succ.calls)
    for i in range(10):
        print('function output : {0}'.format(succ(i)))
    print('calls after execution: {0}'.format(succ.calls))
