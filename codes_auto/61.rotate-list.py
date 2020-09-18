#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] rotate-list
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        length=0
        length_ptr=head
        while length_ptr:
            length_ptr=length_ptr.next
            length+=1
        print(length)
        k=k%length
        
        if k==0:
            return head

        dummy=ListNode(0)
        dummy.next=head
        first=head
        pre=dummy
        second=head
        first_step=k
        while first_step>0:
            first=first.next
            first_step-=1

        while first:
            first=first.next
            pre=second
            second=second.next
        pre.next=None
        new_head=second
        tail=pre
        while second:
            tail=second
            second=second.next

        tail.next=dummy.next
        return new_head

# @lc code=end