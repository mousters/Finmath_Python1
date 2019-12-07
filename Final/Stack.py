import sys
import unittest
from unittest.mock import patch
import io


# Below you will need to create a Node, a Stack, and custom Exceptions which your Node and Stack use. Instructions are provided below, but please refer to the test cases. They will be the most helpful.
class StackError(Exception):
    pass
class StackFullError(Exception):
    pass
class StackEmptyError(Exception):
    pass
class StackIndexError(Exception):
    pass
class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.has_next=False
        if pointer==None:
            self.has_next = False
        else:
            self.has_next=True
        self.__next=pointer
    def __repr__(self):
        return '<Node(data={0}, has_next={1})>'.format(self.data,self.has_next)
    # A node is a container for data and pointer to its successor. Since a node is just a sub object to the stack,
    # the pointer to the node's succussor need to be protected so that the stack can modify it directly, but we need
    # to dissallow outside modification by declaring a next method that acts as an attribute and prohibits modifying next.
    # Finally, we need a representation of the object that looks like <Node(data=<data>, next=<data>)>
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self,pointer):
        self.__next=pointer
        self.has_next=True


class Stack:
    def __init__(self,limit=None):
        self.__top=None
        self.iterator=0
        self.empty=True
        self.maxsize=-1
        self.full=False
        self.size=0
        if limit!=None:
            self.maxsize=limit
    @property
    def top(self):
        return self.__top
    @top.setter
    def top(self,something):
        raise StackError()
    # A stack is a collection of functions that operates on a colleciton of nodes.
    # The linked list of nodes is defined by it's head only. The stack always knows about the "top" node of this linked list
    # and keeps track of it's size. The top attribute should be private, but accessible. This means that you should be able to
    # call stack.top and read its value but not set its value outside the stack. The stack also may limit the amout of nodes it
    # can handle but isn't required to set a limit. A limitless stack size will have a maxsize of -1. You will also need to include
    # properties or attributes, empty and full.
    def push(self,element):
        if self.size>=self.maxsize and self.maxsize!=-1:
            raise StackFullError()
        self.size+=1
        if self.size==self.maxsize:
            self.full=True
        curr=self.__top
        if curr==None:
            self.empty=False
            self.__top=Node(element,None)
        else:
            self.__top=Node(element,None)
            self.__top.next=curr
    def pop(self):
        if self.empty==True:
            raise StackEmptyError()
        if (self.size==1):
            self.empty=True
        self.size-=1
        output=self.__top.data
        self.__top=self.__top.next
        return output

    def peek(self,layer=1):
        if layer>self.size:
            raise StackIndexError()
        nod=self.top
        if layer==1:
            return nod.data
        else:
            for i in range(layer-1):
               nod=nod.next
            return nod.data
    def flush(self):
        self.__top=None
        self.empty=True
        self.full=False
        self.size=0
    # A stack must implement a push and a pop method that adds and removes a data, respectively. A stack must also implement a peek
    # method which allows you to view the top-most element. Peek may also take an argument which allows you to peek x elements deep.

    # A flush method must also be implemented which resets the stack. You may also want to implement a reverse method, which reverses
    # the order of the stack, and a repr method.
    def reverse(self):
        temp_list=[]
        while self.size>0:
            temp_list.append(self.pop())
        for i in range(len(temp_list)):
            self.push(temp_list[i])
    # finally, you will overload the __iter__ and __next__ method which makes the stack iterable. See the test case below.

    def __next__(self):
        if self.iterator >= self.size:
            raise StopIteration()
        ans = self.peek(self.iterator+1)
        self.iterator += 1
        return ans
    # should return the data of the next node when next() invoked on the stack

    def __iter__(self):
        self.iterator=0
        return self

# should set a starting value for __next__ to use and return self


def setup_stack(depth, maxsize=-1):
    # a setup method used in test cases below
    s = Stack(maxsize)
    for i in range(depth):
        s.push(i)
    return s


'''Passed'''
def test_node_design(self):
    n = Node()
    print(n.data)
    print(n.next)
    print(repr(n), "<Node(data=None, has_next=False)>")
    for element in ["Python", n, 3]:
        new_node = Node(element)
        print(new_node.data, element)
        print(new_node.next)
        print(repr(new_node), f"<Node(data={new_node.data}, has_next=False)>")
    n.next = new_node
    print(repr(n), f"<Node(data={n.data}, has_next=True)>")
'''Passed'''
def test_stack_design(self):
    s = Stack()
    self.assertIsNone(s.top)
    self.assertEqual(s.size, 0)
    self.assertEqual(s.maxsize, -1)
    self.assertFalse(s.full)
    s = Stack(100)
    self.assertIsNone(s.top)
    self.assertEqual(s.size, 0)
    self.assertEqual(s.maxsize, 100)
    self.assertTrue(s.empty)
    self.assertFalse(s.full)
'''passed'''
def test_push_method(self):
    s = self.setup_stack(20, 100)
    self.assertTrue(isinstance(s.top, Node))
    self.assertEqual(s.top.data, 19)
    self.assertEqual(s.size, 20)
'''passed'''
def test_top_public_and_private_attribute(self):
    # this test is not critical to passing subsequent unit tests.
    s = Stack()
    with self.assertRaises(AttributeError):
        print(s.__top)
    with self.assertRaises(StackError):
        s.top = Node(3)
'''passed'''
def test_push_to_full_stack_raises_error(self):
    s = self.setup_stack(10, 10)
    with self.assertRaises(StackFullError):
        s.push(100)
def test_pop_method(self):
    s = self.setup_stack(2)
    self.assertEqual(s.pop(), 1)
    self.assertEqual(s.top.data, 0)
    self.assertFalse(s.empty)
    self.assertFalse(s.full)
def test_pop_from_empty_stack_raises_error(self):
    s = self.setup_stack(2)
    for i in range(2):
        self.assertEqual(s.pop(), 2 - (i + 1))
    with self.assertRaises(StackEmptyError):
        s.pop()
def test_peek_no_arg(self):
    s = self.setup_stack(10, 10)
    self.assertTrue(s.full)
    self.assertTrue(s.peek(), 9)
def test_peek_with_arg(self):
    s = self.setup_stack(10, 10)
    self.assertTrue(s.peek(5), 4)
def test_peek_with_large_arg_raises_error(self):
    s = self.setup_stack(10, 10)
    with self.assertRaises(StackIndexError):
        s.peek(11)
def test_flush_method(self):
    s = self.setup_stack(5)
    s.flush()
    self.assertIsNone(s.top)
    self.assertEqual(s.size, 0)

def test_stack_is_an_iterable_generator(self):
    # this test is not critical to passing 'test_reverse_method' but it will help.
    s = self.setup_stack(10)
    self.assertTrue(isinstance(iter(s), Stack))
    self.assertEqual(iter(s).iterator, 0)
    # an iterable object is on that can be handled by python iterators such as enumerate
    for i, data in enumerate(s):
        self.assertEqual(data, s.size - (i + 1))
    # an iterable object must raise StopIteration when you've reached the end of the structure
    s = iter(s)
    for _ in range(10):
        next(s)
    with self.assertRaises(StopIteration):
        next(s)

def test_reverse_method(self):
    s = self.setup_stack(10)
    s.reverse()
    self.assertEqual(s.size, 10)
    self.assertEqual(s.peek(), 0)
    self.assertEqual(s.peek(10), 9)


if __name__ == '__main__':
    test_func = sys.stdin.readline()
    with patch('unittest.runner.time'):
        buf = io.StringIO()
        suite = unittest.TestSuite()
        suite.addTest(StackTests(test_func))
        runner = unittest.TextTestRunner(stream=buf, verbosity=2)
        runner.run(suite)
        sys.stdout.write(buf.getvalue())