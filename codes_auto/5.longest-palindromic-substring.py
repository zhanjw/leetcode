#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] longest-palindromic-substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        res=""
        for i in range(len(s)):
            s1=palindrome(i, i)
            s2=palindrome(i, i+1)
            if len(s1)>len(res):
                res=s1
            if len(s2)>len(res):
                res=s2
        return res

            
# @lc code=end