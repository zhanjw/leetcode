#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] swap-nodes-in-pairs
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def swap(ptr):
    if ptr==None or ptr.next==None or ptr.next.next==None:
        return ptr
    
    prev_node=ptr
    pos1_node=ptr.next
    pos2_node=ptr.next.next
    next_node=ptr.next.next.next
    
    prev_node.next=pos2_node
    pos2_node.next=pos1_node
    pos1_node.next=next_node
    return prev_node
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(float("-inf"))
        dummy.next=head
        ptr=dummy
        while ptr!=None and ptr.next!=None:
            ptr=swap(ptr)
            ptr=ptr.next.next
        return dummy.next

# @lc code=end