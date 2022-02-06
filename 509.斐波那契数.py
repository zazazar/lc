#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start

# 递归
class Solution:
    def fib(self, n: int) -> int:

        if n == 1 or n==2:
            return 1
        if n == 0:
            return 0

        return self.fib(n-1)+self.fib(n-2) 

#动态规划           
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
# @lc code=end
if __name__ =="__main__":
    sol = Solution().fib(5)
    print(sol)
