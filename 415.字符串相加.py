#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(map(int,list(num1)))
        num2 = list(map(int,list(num2)))
        num1.reverse()
        num2.reverse()
      
        result = []
        carry = []
        carry.append(0)
        length = max(len(num1),len(num2))
        for i in range(length):
            x = 0
            y = 0
            if i<len(num1):
                x = num1[i]
            if i<len(num2):
                y = num2[i]

            if x+y+carry[i]>=10:
                carry.append(1)
                result.append(x+y-10+carry[i])
            else:
                carry.append(0)
                result.append(x+y+carry[i])

        if carry[length] == 1:
            result.append(1)

        result.reverse()

        return "".join(str(x) for x in result)
# @lc code=end

