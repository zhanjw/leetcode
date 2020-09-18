#
# @lc app=leetcode.cn id=718 lang=python
#
# [718] maximum-length-of-repeated-subarray
#
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        mx=0
        dp=[[0 for i in range(len(A)+1)] for i in range(len(B)+1)]
        for i,ival in enumerate(A,start=1):
            for j,jval in enumerate(B,start=1):
                if jval==ival:
                    dp[i][j]=dp[i-1][j-1]+1
                    if dp[i][j]>mx:
                        mx=dp[i][j]
                # else: 
                #     dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return mx
# @lc code=end