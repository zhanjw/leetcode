#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] binary-tree-zigzag-level-order-traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans=[]
        queue=[root]
        layer=[]
        reverse_flag=False
        while queue:
            layer=queue[:]
            queue=queue[::-1] if reverse_flag else queue
            reverse_flag=not reverse_flag
            temp=[]
            for i in queue:
                temp.append(i.val)
            ans.append(temp)
            
            queue=[]
            for i in layer:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
        return ans
# @lc code=end