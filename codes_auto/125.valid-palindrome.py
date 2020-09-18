#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] valid-palindrome
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        left,right=0,len(s)-1
        left_count=0
        right_count=0
        while left<right:
            print(left,right,s[left],s[right])
            if ('a'<=s[left]<='z' or '0'<=s[left]<='9')and('a'<=s[right]<='z' or '0'<=s[right]<='9'): 
                if s[left]==s[right]:
                    left_count+=1
                    right_count+=1
                    left+=1
                    right-=1
                else:
                    return False
            elif not ('a'<=s[left]<='z' or '0'<=s[left]<='9'):
                left+=1
            else:
                right-=1
        if left_count==right_count:
            return True
        else:
            return False
# @lc code=end