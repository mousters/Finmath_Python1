import itertools
#convert string to integer
def to_integer(num):
    ans=0
    for i in num:
        ans*=10
        ans+=int(i)
    return ans
#
def checkDivisibility(arr,divisor):
    divisor=int(divisor)
    ans=[]
    for i in arr:
        if(len(str(i))<=3):
            perm_temp=itertools.permutations(str(i))
        else:
            perm_temp = itertools.permutations(str(i),3)
        check="NO"
        for j in perm_temp:
            if to_integer(j)%divisor==0:
                check="YES"
                break
        ans.append(check)
    return ans
if __name__=='__main__':
    divisor=input('What number do you want to divide it by : ')
    #the goal of the question is to check if by anyway, the number can be divided by 8, for example
    #61, after permutation, 16 can be divided by 8, 42 --> 24/8=3
    #but 75 or 57 can not be divided by 8
    print(checkDivisibility([61,75,42],divisor))
