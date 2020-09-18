#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] maximum-product-subarray
#
class Solution(object):
    # 本题考查动态回归，难点就是动态方程的归纳
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 初始化子序列最大的乘积
        product = nums[0]
        # 这两个数组用来分别记录不同子序列的最大值和最小值
        max_num, min_num = [1] * (len(nums)+1), [1] * (len(nums)+1)
        for i in range(len(nums)):
            # 以下两步是状态转移方程
            max_num[i+1] = max(max_num[i]*nums[i], min_num[i]*nums[i], nums[i])
            min_num[i+1] = min(max_num[i]*nums[i], min_num[i]*nums[i], nums[i])
            product = max(product, max_num[i+1])
        return product
# @lc code=end