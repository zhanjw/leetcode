#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] merge-k-sorted-lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def insort_node(a, x):
            lo,hi=0,len(a)
            while lo < hi:
                mid = (lo+hi)//2
                if a[mid].val < x.val: lo = mid+1
                else: hi = mid
            a.insert(lo, x)
        while None in lists:
            lists.remove(None)
        lists.sort(cmp=lambda a,b:a.val-b.val)
        head=ListNode(0)
        ptr=head
        while len(lists)>1:
            node=lists.pop(0)
            if node:
                ptr.next,ptr,node=node,node,node.next
            if node:
                insort_node(lists,node)
        if len(lists)>0:
            ptr.next=lists[0]
        return head.next
# @lc code=end