#
# @lc app=leetcode.cn id=260 lang=python
#
# [260] single-number-iii
#
class Solution:
    def singleNumber(self, nums):
        if not nums: return []
        temp = 0            # 所有元素与0异或时，结果均不变
        for num in nums:
            temp ^= num
        idx = 0              # 获取temp中最低位1的位置
        while temp & 1 ==0:
            temp = temp>>1
            idx += 1
        a = b = 0
        for num in nums:
            if self.isBit(num,idx):
                a ^=num
            else:
                b ^=num
        return [a,b]

    def isBit(self,num,idx):   # 判断num的二进制从低到高idx位是不是1
        num = num>>idx
        return num & 1
# @lc code=end