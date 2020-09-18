#
# @lc app=leetcode.cn id=237 lang=python
#
# [237] delete-node-in-a-linked-list
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val # 前移待删除节点的后一个节点的值
        node.next = node.next.next # 更新待删除节点的指针

# @lc code=end