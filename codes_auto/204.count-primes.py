#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] count-primes
#
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrim = [True]*n;
        for i in range(2,int(sqrt(n)+1)):
            if isPrim[i]:
                for j in range(i*i,n,i):
                    isPrim[j]=False
        count=0
        for i in range(2,n):
            if isPrim[i]:
                count+=1
        return count
# @lc code=end