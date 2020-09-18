#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] same-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        left=self.isSameTree(p.left,q.left)
        right=self.isSameTree(p.right,q.right)
        return p.val==q.val and left and right
# @lc code=end