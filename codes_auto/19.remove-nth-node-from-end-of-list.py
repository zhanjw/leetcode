#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] remove-nth-node-from-end-of-list
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ll=[]
        dummy=ListNode(0)
        dummy.next=head
        ptr=dummy
        while ptr.next:
            ll.append(ptr)
            ptr=ptr.next
        ll.append(ptr)
        if -n+1==0:
            ll[-n-1].next=None
        else:
            ll[-n-1].next=ll[-n+1]
        return dummy.next
# @lc code=end