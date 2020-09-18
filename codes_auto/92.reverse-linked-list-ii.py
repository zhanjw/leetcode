#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] reverse-linked-list-ii
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        def reverse_driver(head,n):
            pre=None
            ptr=head
            nn=n
            while nn>m:
                pre=ptr
                ptr=ptr.next
                nn-=1
            pre=ptr.next
            ptr=head
            nn=n
            while ptr and nn>m:
                nex=ptr.next
                ptr.next=pre
                pre=ptr
                ptr=nex
                nn-=1
            ptr.next=pre
            return ptr
        if m==1 and n==1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        ptr=dummy
        mm=m
        while mm>0:
            pre=ptr
            ptr=ptr.next
            mm-=1
        pre.next=reverse_driver(ptr,n)
        return dummy.next
# @lc code=end