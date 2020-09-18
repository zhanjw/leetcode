#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] implement-queue-using-stacks
#
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=[]
        self.tail=[]
        self.peak=None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.roll(self.tail,self.head)
        self.head.append(x)
        self.roll(self.head,self.tail)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.tail.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.tail[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.tail==[]
    
    def roll(self,a,b):
        while a!=[]:
            b.append(a.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end