#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] symmetric-tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _isSymmetric(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val==root2.val:
            # print(root1.val,root2.val)
            if self._isSymmetric(root1.left,root2.right) and self._isSymmetric(root1.right,root2.left):
                return True
        return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self._isSymmetric(root.left,root.right)
# @lc code=end