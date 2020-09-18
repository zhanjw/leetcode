#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] flatten-binary-tree-to-linked-list
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _flatten(self, root):
        if root:
            if root.left and root.right:
                left_head,left_tail=self._flatten(root.left)
                right_head,right_tail=self._flatten(root.right)
                root.left, root.right=None,left_head
                left_tail.left,left_tail.right=None,right_head
                return root,right_tail
            elif root.left and not root.right:
                left_head,left_tail=self._flatten(root.left)
                root.left,root.right=None,left_head
                return root,left_tail
            elif not root.left and root.right:
                right_head,right_tail=self._flatten(root.right)
                root.left,root.right=None,right_head
                return root,right_tail
            else:return root,root
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self._flatten(root)
        
# @lc code=end