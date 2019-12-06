import numpy as np
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
def depth_first(node,list):
    if(node==None):
        return
    else:
        if(node.left !=None):
            list.append(node.left.value)
            depth_first(node.left,list)
        elif node.right!=None:
            list.append('NA')
        if (node.right != None):
            list.append(node.right.value)
            depth_first(node.right,list)
        elif node.left!=None:
            list.append('NA')
    return list
class Tree:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root

    def add(self, value):
        if (self.root == None):
            self.root = Node(value)
        else:
            self._add(value, self.root)
    def _add(self, value, node):
        if (value < node.value):
            if (node.left != None):
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if (node.right != None):
                self._add(value, node.right)
            else:
                node.right = Node(value)
    def __repr__(self):
        pass
#check if the output follows the depth-first printing of the tree
def valid_helper(a):
    #only 1 node in the tree
    if(len(a)<=1):
        return True

    #assume to be true
    check=True
    root=a[0]
    left=[]
    right=[]

    #large meaning the larger the side, so large= false --> check the left side first
    large=False
    for i in range(len(a)-1):
        #if value is smaller than the root, meaning it is on the smaller side
        if a[i+1]<root and large==False:
            left.append(a[i+1])
        else:
            #if on the larger side
            if(large):
                #if on the large side, the value is smaller than root, then it is mistakenly placed
                if a[i+1]<root:
                    check=False
            #if large is false then this means that we encounter a value larger than the root
            #so if the array is correctly positioned, we have moved to the larger side
            large=True
            right.append(a[i+1])
    #now if check did not become false, everything smaller than root is on the array left
    #and everything larger is in the array right, do the check again
    if (check == False):
        return False
    check=valid_helper(left)
    if(check==False):
        return False
    check = valid_helper(right)

    return check

if __name__=='__main__':
    t=Tree()
    nodes=[3, 2 ,1, 5, 4, 6]
    for i in nodes:
        t.add(i)
    depth_repr=depth_first(t.getRoot(),[nodes[0]])
    print(depth_repr)
    #[3, 2, 1, 'NA', 5, 4, 6]
    print('homework printing check')
    print(valid_helper([3, 2 ,1, 5, 4, 6]))
    #T
    print(valid_helper([1,3,4,2] )) #false
    print(valid_helper([3,4,5,1,2]))  #false

