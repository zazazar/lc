#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'

        result = []
        curresult = []
        carry = []
        carry.append(0)
        remainder = 0

        num1 = list(num1)
        num1 = list(map(int,num1))
        num1.reverse()
        # print(num1)
        num2 = list(num2)
        num2 = list(map(int,num2))
        num2.reverse()

        for i in range(len(num2)):
            # 补0
            for x in range(i):
                curresult.append(0)
            for j in range(len(num1)):
                temp = num2[i]*num1[j]+carry[j]
                carry.append(temp//10)
                remainder = temp%10
                curresult.append(remainder)
            if carry[j+1] != 0:
                curresult.append(carry[j+1])

            curresult.reverse()
            result.append(curresult)
            # 清空
            curresult = []
            carry = []
            carry.append(0)

        result2 = self.addall(result)

        return "".join(str(x) for x in result2)

    def addall(self,nums):
        current = [0]
        for index,x in enumerate(nums):
            one = self.add(current,x)
            current = one
        return current

    def add(self,num1:List[int],num2:List[int]):
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

        return result

# @lc code=end
if __name__ == "__main__":
    sol = Solution().multiply('321','437')
    print(sol)
    print(Solution().addall([[1,1,8,7,7],[1,2,8,4,0,0]]))
    # str = [1,2,3]

