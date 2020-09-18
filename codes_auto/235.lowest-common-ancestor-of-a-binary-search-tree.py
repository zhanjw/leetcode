#
# @lc app=leetcode.cn id=235 lang=python
#
# [235] lowest-common-ancestor-of-a-binary-search-tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val>q.val:
            p,q=q,p
        while root:
            if q.val<root.val:
                root=root.left
            elif p.val>root.val:
                root=root.right
            else:
                return root
# @lc code=end