# find all the characters(including space,punctuation...) that have indexes with even values (0,2,4,6,8,....) in a given string
# return a string
# "a1b2c3" ->"abc"
def test1(string):
    res = ''
    for i in range(len(string)):
        if i % 2 == 0:
            res += string[i]
    return res


# return the substring upto a given character c
# if not, return the whole string
# input: "abcd" and "d"
# output: "abc"
# input: "abcd" and "e"
# output: "abcd"
def test2(string, c):
    if c in string:
        res = string.split(c)[0]
    else:
        res = string
    return res


# use generator to create a sequence of dictionaries
# key is integer starting from 1, value is the square of key
def test3(max_key):
    dic = {}
    for i in range(1, max_key + 1):
        dic[i] = i ** 2
        yield dic


# extract main diagonal of square matrix
# return a diagonal matrix
# [[1,2,3],        [[1,0,0],
#  [4,5,6],   ->    [0,5,0],
#  [7,8,9]]         [0,0,9]]
def test4(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if i != j:
                matrix[i][j] = 0
    return matrix


# standardize a dataset
# each column vector in the matrix represents samples of one random variable
# you need to normalize each sample data so that mean = 0 and variance = 1
# input is a matrix and return should be a matrix
def test5(matrix):
    for j in range(len(matrix[0])):

        new_lst = []
        tot = 0
        for i in range(len(matrix)):
            new_lst.append(matrix[i][j])
        avg = sum(new_lst) / len(new_lst)

        for m in range(len(new_lst)):
            tot += (new_lst[m] - avg) ** 2
        std = (tot / (len(new_lst) - 1)) ** (1 / 2)

        for n in range(len(new_lst)):
            new_lst[n] = (new_lst[n] - avg) / std
            matrix[n][j] = new_lst[n]

    return matrix
