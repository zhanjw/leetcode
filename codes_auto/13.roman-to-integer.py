#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] roman-to-integer
#
class Solution(object):
    def romanToInt(self, s):
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=0
        for i in range(len(s)-1):
            temp=roman[s[i]]
            if roman[s[i]]>=roman[s[i+1]]:
                result=result+temp
            else:
                result=result-temp
        return result+roman[s[-1]]
# @lc code=end