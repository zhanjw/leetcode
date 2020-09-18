#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] lowest-common-ancestor-of-a-binary-tree
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
        dicts = {root:None}
        stack=[root]
        while stack:
            curr_node=stack.pop()
            if curr_node.right:
                dicts[curr_node.right]=curr_node
                stack.append(curr_node.right)
            if curr_node.left:
                dicts[curr_node.left]=curr_node
                stack.append(curr_node.left)
        l1=p
        l2=q
        while l1!=l2:
            l1=dicts.get(l1,q)
            l2=dicts.get(l2,p)
        return l1
# @lc code=end