def call_counter(func):
    print('decorator called')
    def helper(x):
        # '''this is initialize here, throught +=1, but now the helper does not have any value'''
        # '''bc before this code is called, the helper.calls will be intialize to 0 below'''

        helper.calls += 1
        print('decorator called :{0}'.format(helper.calls))
        return func(x)
    helper.calls = 0
    return helper
