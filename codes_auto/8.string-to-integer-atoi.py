#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] string-to-integer-atoi
#
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        def trim(str):
            i=0
            while len(str)>i and str[i]==" ":
                i+=1
            return str[i:]
        def isdigit(n):
            return n>="0" and  n<="9"
        def scale(n):
            if n<-2**31:
                return -2**31
            if n>2**31-1:
                return 2**31-1
            return n
        def char2int(n):
            if n=="0": return 0
            if n=="1": return 1
            if n=="2": return 2
            if n=="3": return 3
            if n=="4": return 4
            if n=="5": return 5
            if n=="6": return 6
            if n=="7": return 7
            if n=="8": return 8
            if n=="9": return 9
            return -1
        def core(str):
            num=0
            num_str=[]
            for i in str:
                if isdigit(i):
                    num_str.append(i)
                else:
                    break
            for i in num_str:
                num=10*num+char2int(i)
            return num

        str=trim(str)
        if len(str)==0:
            return 0
        if len(str)>0 and not (isdigit(str[0]) or str[0]=="-" or str[0]=="+"):
            return 0
        if len(str)>1 and (str[0]=="-" or str[0]=="+") and not isdigit(str[1]):
            return 0
        if str[0]=="-":
            num=-core(str[1:])
        elif str[0]=="+":
            num=core(str[1:])
        else:
            num=core(str)
        return scale(num)
# @lc code=end