#
# @lc app=leetcode.cn id=12 lang=python
#
# [12] integer-to-roman
#
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_count=[[0,1000,'M'],[0,900,'CM'],[0,500,'D'],[0,400,'CD'],[0,100,'C'],[0,90,'XC'],[0,50,'L'],[0,40,'XL'],[0,10,'X'],[0,9,'IX'],[0,5,'V'],[0,4,'IV'],[0,1,'I']]
        roman_str=""
        for i in roman_count:
            i[0]=num//i[1]
            num-=i[0]*i[1]
            roman_str+=i[0]*i[2]
        return roman_str
# @lc code=end