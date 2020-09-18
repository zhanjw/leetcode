#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] diameter-of-binary-tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recursion(node):
            if not node:
                return 0,0
            max_len_left,deep_left = recursion(node.left)
            max_len_right,deep_right = recursion(node.right)
            manx_len = max(max_len_left, max_len_right, deep_left+deep_right)
            deep = max(deep_left,deep_right) + 1
            return manx_len,deep

        return recursion(root)[0]

# @lc code=end