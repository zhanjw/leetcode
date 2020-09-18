#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] reverse-linked-list
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None:
        #     return head
        # ptr=head
        # nex=ptr.next
        # ptr.next=None
        # while nex:
        #     prev=ptr
        #     ptr=nex
        #     nex=nex.next
        #     ptr.next=prev
        # return ptr
        dummy=ListNode(float("-inf"))
        while head:
            dummy.next,head.next,head=head,dummy.next,head.next
        return dummy.next
# @lc code=end