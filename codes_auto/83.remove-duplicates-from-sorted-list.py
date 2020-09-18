#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] remove-duplicates-from-sorted-list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        slow=head
        fast=slow.next
        while fast:
            if slow.val!=fast.val:
                slow=slow.next
                slow.val=fast.val
            fast=fast.next
        slow.next=None
        return head
# @lc code=end