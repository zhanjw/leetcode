#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] recover-binary-search-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = []
        def get_inorder(node):
            if not node:
                return
            get_inorder(node.left)
            inorder.append(node)
            get_inorder(node.right)
        get_inorder(root)

        first,second,prev = None,None,TreeNode(-float('inf'))
        #因为是二叉搜索树 中序遍历出来是单调递增的 所以我们只需要找2个不满足比前一个大的结点
        #first存第一个不满足的点 second存第二个不满足的点
        for i,curr in enumerate(inorder):
            #如果没有出现过异常点，并且前一个结点比当前节点大 1 5 4 3 2 中 5>4 5为第一个异常点
            if not first and prev.val>curr.val:
                first = prev
            #如果已经有一个异常点，并且前一个结点比当前节点大 1 5 4 3 2 中 3>2 2为第二个异常点
            if first and prev.val>curr.val:
                second = curr
            #prev更新为当前结点作为下一个点的 前继结点
            prev = curr
        first.val,second.val = second.val,first.val

# @lc code=end