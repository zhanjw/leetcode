#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] minimum-window-substring
#
from collections import Counter
from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left, right = 0, 0
        ans = s + s
        target = Counter(t)
        curr_status = defaultdict(int)
        match = 0

        def contains(counter, target):
            if len(counter) < len(target):
                return False
            for k in counter:
                if k not in target or counter[k] < target[k]:
                    return False
            return True

        while right < len(s):
            if s[right] in target:
                curr_status[s[right]] += 1
                if curr_status[s[right]] == target[s[right]]:
                    match += 1
            # while left < len(s) and contains(curr_status, target):
            while left < len(s) and match == len(target):
                if right - left + 1 < len(ans):
                    ans = s[left:right + 1]
                if s[left] in target:
                    curr_status[s[left]] -= 1
                    if curr_status[s[left]] < target[s[left]]:
                        match -= 1
                left += 1
            right += 1
        return "" if ans == s + s else ans
# @lc code=end