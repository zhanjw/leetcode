#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] palindrome-linked-list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        fast, slow, prev=head, head, None
        while fast and fast.next:
            fast=fast.next.next
            tmp=slow.next
            slow.next=prev
            prev, slow=slow, tmp
            
        left, right=prev, slow
        if fast:
            right=slow.next
        while left:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True

# @lc code=end