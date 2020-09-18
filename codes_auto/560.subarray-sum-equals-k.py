#
# @lc app=leetcode.cn id=560 lang=python
#
# [560] subarray-sum-equals-k
#
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixSumArray = {0:1}
        count = 0
        prefixSum = 0
        
        for ele in nums:
            prefixSum += ele
            subArray = prefixSum - k
            
            if subArray in prefixSumArray:
                count += prefixSumArray[subArray]
            '''
            prefixSumArray.get(prefixSum, 0)
            在hash table里查找key，如果有返回对应的value，反之返回0 
            '''
            prefixSumArray[prefixSum] = prefixSumArray.get(prefixSum, 0) + 1
        
        return count
# @lc code=end