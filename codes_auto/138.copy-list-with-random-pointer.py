#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] copy-list-with-random-pointer
#
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dts={}
        new_head=Node(0)
        ptr=head
        new_ptr=new_head
        while ptr:
            dts[ptr]=Node(ptr.val)
            new_ptr.next=dts[ptr]
            ptr=ptr.next
            new_ptr=new_ptr.next
        ptr=head
        new_ptr=new_head.next
        while new_ptr:
            if ptr.random:
                new_ptr.random=dts[ptr.random]
            ptr=ptr.next
            new_ptr=new_ptr.next
        return new_head.next
# @lc code=end