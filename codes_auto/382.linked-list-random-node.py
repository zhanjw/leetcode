#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] linked-list-random-node
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 0
        ptr = self.head
        res = 0
        while ptr:
            count += 1
            if random.randint(1, count) == count:
                res = ptr.val
            ptr = ptr.next
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end