#
# @lc app=leetcode.cn id=143 lang=python
#
# [143] reorder-list
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # if not head or not head.next or not head.next.next:
        #     return head
        # dummy=ListNode(0)
        # dummy.next=head
        # ptr=dummy.next
        # head=ptr
        # pre=head
        # cur=pre
        # while cur:
        #     cur=pre.next
        #     pre.next=None
        #     while cur and cur.next:
        #         nex=cur.next
        #         if pre==head:
        #             cur.next=None
        #         else:
        #             cur.next=pre
        #         pre=cur
        #         cur=nex
        #     head.next=cur if cur else pre
        #     head=head.next
        if not head:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        p = slow.next
        tail = slow.next
        slow.next = None

        p = self.reverseList(p)
        m = head
        while p:
            m.next, p.next, m, p = p, m.next, m.next, p.next

    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
# @lc code=end