#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] sort-list
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        res = h = ListNode(0)
        while left and right:
            if left.val < right.val: 
                h.next, left = left, left.next
            else: 
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

# @lc code=end