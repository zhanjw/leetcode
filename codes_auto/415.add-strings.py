#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] add-strings
#
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        idx1=len(num1)-1
        idx2=len(num2)-1
        res=[]
        borrow=0
        while idx1>=0 and idx2>=0:
            tmp=int(num1[idx1])+int(num2[idx2])+borrow
            borrow=0
            idx1-=1
            idx2-=1
            if tmp>9:
                tmp-=10
                borrow=1
            res.append(str(tmp))
        while idx1>=0:
            tmp=int(num1[idx1])+borrow
            borrow=0
            idx1-=1
            if tmp>9:
                tmp-=10
                borrow=1
            res.append(str(tmp))
        while idx2>=0:
            tmp=int(num2[idx2])+borrow
            borrow=0
            idx2-=1
            if tmp>9:
                tmp-=10
                borrow=1
            res.append(str(tmp))
        if borrow==1:
            res.append(str(borrow))
        return ''.join(res[::-1])
# @lc code=end