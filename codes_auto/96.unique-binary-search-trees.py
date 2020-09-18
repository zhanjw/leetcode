#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] unique-binary-search-trees
#
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 动态规划
        # g[n] 表示长为n的二叉搜索树的数量

        # 边界条件
        g = [0] * (n+1)
        g[0] = 1 
        g[1] = 1
        
        # 自底向上 动态规划
        for i in range(2, n+1):
            # 确定长为i的树的 左右子树的长度（最小为0， 最大为i-1）
            for j in range(i):
                g[i] += g[j] * g[i-j-1] # 左树种数 * 右树种数
        return g[n]
# @lc code=end