#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] merge-two-sorted-lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(float("-inf"))
        head=dummy
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                head.next,head,l1=l1,l1,l1.next
            else:
                head.next,head,l2=l2,l2,l2.next
        head.next=l1 if l1!=None else l2
        return dummy.next
# @lc code=end