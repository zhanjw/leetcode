#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] balanced-binary-tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        depth=self._isBalanced(root)
        if depth==-1:
            return False
        return True
    def _isBalanced(self, root):
        if not root:
            return 0
        left=self._isBalanced(root.left)
        right=self._isBalanced(root.right)
        if abs(left-right)>1 or left==-1 or right==-1:
            return -1
        return max(left,right)+1
# @lc code=end