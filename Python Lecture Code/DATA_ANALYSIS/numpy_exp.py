import numpy as np

if __name__=='__main__':
    #OUTPUT AT THE BOTTOM
    #create a list
    list_num=[2,31,2,3]
    x=np.array(list_num)
    # create a matrix with 4* 3 dimension of zeros
    x=np.zeros([4,3])
    # create a matrix with 4* 3 dimension of ones
    x = np.ones([4, 3])
    # create a list start from 1 to 10
    x=np.arange(10)
    # create a list start from 1 and takes 4 steps to reach 10, which are 1, 4, 7 10
    x=np.linspace(1,10,4)
    # square every number in x
    x**2
    #return T or F based on if the number >5
    x>5
    #select the number that passed the criterion (>5)
    x[x>5]
    #make the number into 2 x 2 matrix form
    a = np.array([1, 0, 0, 1]).reshape(2, 2)
    #similar logic
    b = np.arange(4).reshape(2, 2)
    #2 x 2 identity matrix
    b=np.eye(2)
    #trace of the identity matrix
    np.trace(b)
    #normal multiplication
    b*a
    #dot product
    np.dot(b,a)
    #create random arrays
    x=np.random.random((2,3))
    #max of all number
    x.max()
    #which column is largest
    x.max(axis=0)
    x.max(axis=1)
    #read the text, since the file is absent, cannot run
    x=np.loadtxt('some.csv',delimiter=',')

#
# x=np.array(list_num)
# [ 2 31  2  3]
# x=np.zeros([4,3])
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
# x = np.ones([4, 3])
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]
# x=np.arange(10)
# [0 1 2 3 4 5 6 7 8 9]
# x=np.linspace(1,10,4)
# [ 1.  4.  7. 10.]
# x**2
# [  1.  16.  49. 100.]
# x>5
# [ 1.  4.  7. 10.] [False False  True  True]
# x[x>5]
# [ 1.  4.  7. 10.] [ 7. 10.]
# a=np.array ([1,0,0,1]).reshape(2,2)
# [[1 0]
#  [0 1]]
# b=np.arange(4).reshape(2,2)
# [[0 1]
#  [2 3]]
# b=np.eye(2)
# # [[1. 0.]
# #  [0. 1.]]
# np.trace(b)
# 2.0
# b*a
# [[0 0]
#  [0 3]]
# np.dot(b, a)
# [[0 1]
#  [2 3]]
# x=np.random.random((2,3))
x=np.random.random((2,3))
# x.max(axis=0)
# # [0.41746868 0.50591033 0.52888465]
# x.max(axis=1)
# # [0.50591033,0.52888465]
