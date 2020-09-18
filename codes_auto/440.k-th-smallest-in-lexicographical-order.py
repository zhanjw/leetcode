#
# @lc app=leetcode.cn id=440 lang=python
#
# [440] k-th-smallest-in-lexicographical-order
#
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def cal_steps(n, n1, n2):
            step = 0
            while n1 <= n:
                step += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return step
                
        cur = 1
        k -= 1
        
        while k > 0:
            steps = cal_steps(n, cur, cur + 1)
            # print(steps,k)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10
        
        return cur
# @lc code=end