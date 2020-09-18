#
# @lc app=leetcode.cn id=437 lang=python
#
# [437] path-sum-iii
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _dfs(self,node,sum,target):
        if not node:
            return 0
        l,r=0,0
        target=[node.val]+[each + node.val for each in target]
        l=self._dfs(node.left,sum,target)
        r=self._dfs(node.right,sum,target)
        return target.count(sum)+l+r
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self._dfs(root,sum,[]) if root else 0
# @lc code=end