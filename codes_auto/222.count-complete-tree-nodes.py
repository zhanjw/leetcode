#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] count-complete-tree-nodes
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth=0
        while root:
            root=root.left
            depth+=1
        return depth
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth,rightDepth=self.countDepth(root.left),self.countDepth(root.right)
        if leftDepth>rightDepth:
            return (1<<rightDepth)+self.countNodes(root.left)
        else:
            return (1<<leftDepth)+self.countNodes(root.right)
# @lc code=end