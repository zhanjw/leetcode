#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] palindrome-number
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = int(str(abs(x))[::-1])
        #print([x,reverse])
        if x==reverse:
            return True
        return False
# @lc code=end