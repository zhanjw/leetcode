#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] intersection-of-two-linked-lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hA=headA
        hB=headB
        A_once=True
        B_once=True
        while headA and headB and headA != headB:
            headA=headA.next
            headB=headB.next
            if not headA and A_once:
                headA=hB
                A_once=False
            if not headB and B_once:
                headB=hA
                B_once=False
        return headA if headA==headB else None
# @lc code=end