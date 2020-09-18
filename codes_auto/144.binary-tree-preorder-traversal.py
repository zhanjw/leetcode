#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] binary-tree-preorder-traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rt=[]
        stack=[root]
        while stack:
            item=stack.pop()
            rt.extend([item.val])
            if item.right:
                stack.append(item.right)
            if item.left:
                stack.append(item.left)
        return rt
# @lc code=end