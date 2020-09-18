#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] find-all-anagrams-in-a-string
#
from collections import Counter
from collections import defaultdict


class Solution(object):
    def findAnagrams(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = 0
        r = 0
        # ans = s + s
        n = len(s)
        target = Counter(t)
        window = defaultdict(lambda: 0)
        match = 0
        res = []

        def contains(counter, target):
            if len(counter) < len(target):
                return False
            for k in counter:
                if k not in target or counter[k] < target[k]:
                    return False
            return True

        while r < n:
            if s[r] in target:
                window[s[r]] += 1
                if window[s[r]] == target[s[r]]:
                    match += 1
            # while l < n and contains(window, target):
            r += 1
            while l < n and match == len(target):
                if r - l == len(t):
                    # ans = s[l:r + 1]
                    res.append(l)
                if s[l] in target:
                    window[s[l]] -= 1
                    if window[s[l]] < target[s[l]]:
                        match -= 1
                l += 1
        return res

# @lc code=end