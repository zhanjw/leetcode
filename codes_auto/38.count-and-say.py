#
# @lc app=leetcode.cn id=38 lang=python
#
# [38] count-and-say
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def count(n):
            count_list = []
            idx = 0
            count = 0
            while len(n) > idx + 1:
                if n[idx] != n[idx + 1]:
                    count_list.append(str(count + 1))
                    count_list.append(str(n[idx]))
                    count = -1
                count += 1
                idx += 1
            count_list.append(str(count + 1))
            count_list.append(str(n[idx]))
            return count_list
        result = "1"
        for i in range(1, n):
            result = count(result)
        return "".join(result)
# @lc code=end