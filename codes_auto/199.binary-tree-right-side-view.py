#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] binary-tree-right-side-view
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        output=[]
        deque=[]
        temp=[root]
        while temp:
            deque=temp
            temp=[]
            for index,curr in enumerate(deque):
                if index==0:
                    output.append(curr.val)
                if curr.right:
                    temp.append(curr.right)
                if curr.left:
                    temp.append(curr.left)
        return output
# @lc code=end