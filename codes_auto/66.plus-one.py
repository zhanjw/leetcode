#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] plus-one
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=1
        while True:
            if i<len(digits)+1:
                digits[-i]+=1
            else:
                digits.insert(0,1)
                break
            if digits[-i]>9:
                digits[-i]=0
                i+=1
            else:
                break
        return digits
# @lc code=end