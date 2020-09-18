#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] binary-tree-inorder-traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        if not root:
            return []
        # stack.append(root)
        result=[]
        current_node=root
        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node=current_node.left
            current_node=stack.pop()
            result.append(current_node.val)
            current_node=current_node.right
        return result
# @lc code=end