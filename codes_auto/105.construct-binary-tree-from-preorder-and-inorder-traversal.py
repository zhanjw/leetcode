#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] construct-binary-tree-from-preorder-and-inorder-traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        if len(preorder)==1 and len(inorder)==1:
            return TreeNode(preorder[0])

        root_val=preorder[0]
        root=TreeNode(root_val)

        left_inorder=inorder[:inorder.index(root_val)]
        left_preorder=preorder[1:len(left_inorder)+1]
        root.left=self.buildTree(left_preorder, left_inorder)
        # print(left_preorder,left_inorder)
        right_inorder=inorder[inorder.index(root_val)+1:]
        right_preorder=preorder[len(left_inorder)+1:]
        root.right=self.buildTree(right_preorder, right_inorder)
        # print(right_preorder,right_inorder)
        return root
# @lc code=end