#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] reverse-nodes-in-k-group
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseDriver(self, start, end):
        cur=start
        pre=None
        while cur and cur!=end:
            nex=cur.next
            cur.next=pre
            pre=cur
            cur=nex
        return pre,start

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k<=1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        memory=dummy
        start=head
        cur=head
        i=0
        while cur or i==k:
            if i==k:
                s,e=self.reverseDriver(start,cur)
                memory.next=s
                e.next=cur
                memory=e
                start=cur
                i=0
            if cur:
                cur=cur.next
            i+=1
        return dummy.next
# @lc code=end