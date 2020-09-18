#
# @lc app=leetcode.cn id=43 lang=python
#
# [43] multiply-strings
#
class Solution(object):
  def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    results = []
    for i in range(len(num1)+len(num2)):
        results.append(0)
    for i in range(len(num1)-1,-1,-1):
        for j in range(len(num2)-1,-1,-1):
            #这里有个细节，对于字符串需要先计算最小的一位，先计算后面的
            #数位有利于进位加到前面的数值中去
            p1,p2 = i+j,i+j+1
            mul = ((ord(num1[i]))-((ord('0'))))*((ord(num2[j]))-((ord('0'))))
            sums = mul+results[p2]
            results[p2] = sums%10
            results[p1] = results[p1]+sums//10
            #注意这里有个细节，必须先计算i+j+1后面一位的数值，再计算前面一位
            #i+j的数值，这样方便于把后面的数值带来的进位加到前面数值的上面
    cur = 0
    while cur < len(results) and results[cur] == 0:
        cur += 1
    #去除前导0
    resultstring = ''
    for i in range(cur,len(results)):
      resultstring = resultstring+(str)(results[i])
    if resultstring == '':
      return '0'
    return resultstring

# @lc code=end