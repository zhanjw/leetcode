#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] validate-binary-search-tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _Valid(self, root, mi, ma):
        if not root:
            return True
        val=root.val
        if mi<val<ma:
            left=root.left
            right=root.right
            if self._Valid(left,mi,min(ma,val)) and self._Valid(right,max(mi,val),ma):
                return True
        return False
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._Valid(root,float('-inf'),float('inf'))
# @lc code=end