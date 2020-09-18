#
# @lc app=leetcode.cn id=124 lang=python
#
# [124] binary-tree-maximum-path-sum
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path_sum = float('-inf')

        def dfs(node):
            if not node:  # 边界情况
                return 0
            left = dfs(node.left)  # 对左右节点dfs
            right = dfs(node.right)
            cur_max = max(
                node.val,
                node.val + left,
                node.val + right,
            )
            # 更新全局变量
            self.max_path_sum = max(self.max_path_sum, cur_max, node.val + left + right)
            return cur_max

        dfs(root)
        return self.max_path_sum
        
# @lc code=end