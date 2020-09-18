#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] linked-list-cycle-ii
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return None
        fast=head
        slow=head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
        if fast and fast.next and fast.next.next:
            fast=head
            while fast!=slow:
                # print(fast.val,slow.val)
                fast=fast.next
                slow=slow.next
            return fast
        else:
            return None
# @lc code=end