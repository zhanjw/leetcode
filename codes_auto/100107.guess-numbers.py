#
# @lc app=leetcode.cn id=100107 lang=Python3
#
# [100107] guess-numbers
#
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        idx=0
        count=0
        while idx<len(guess):
            if guess[idx]==answer[idx]:
                count+=1
            idx+=1
        return count
# @lc code=end