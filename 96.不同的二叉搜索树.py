#
# @lc app=leetcode.cn id=96 lang=python3
#
#

# @lc code=start
class Solution:
    def __init__(self):
        self.resArr = [0 for i in range(25)]
        self.resArr[0] = 1
        self.resArr[1] = 1
        self.resArr[2] = 2

    def numTrees1(self,n) :
        if n == 1 or n == 0:
            return 1
        elif n == 2:
            return 2
        res = 0
        for i in range(n):
            if self.resArr[i]!=0:
                x = self.resArr[i]
            else:
                x = self.numTrees(i)

            if self.resArr[n-1-i]!=0:
                y = self.resArr[n-1-i]
            else:
                y = self.numTrees(n-1-i)

            res = res + x * y
            self.resArr[n] = res
        return res

    def numTrees(self,n) :
        for i in range(3, n+1):
            for j in range(0, i):
                self.resArr[i] += self.resArr[j] * self.resArr[i-j-1]
        # print(self.resArr)
        return self.resArr[n]
        
# @lc code=end
print(Solution().numTrees(5)) 


