#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] house-robber-iii
#
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return [0,0]
            left = dfs(node.left)
            right = dfs(node.right)
            return [0+max(left)+max(right), node.val+left[0]+right[0]]
            #当前节点不抢，当前节点抢

        return max(dfs(root))
# @lc code=end