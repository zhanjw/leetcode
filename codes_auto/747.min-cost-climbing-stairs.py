#
# @lc app=leetcode.cn id=747 lang=python
#
# [747] min-cost-climbing-stairs
#
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        costsum=[0]*len(cost)
        costsum[0],costsum[1]=cost[0],cost[1]
        for idx in range(2,len(costsum)):
            costsum[idx]=min(costsum[idx-1],costsum[idx-2])+cost[idx]
        return min(costsum[-1],costsum[-2])
# @lc code=end