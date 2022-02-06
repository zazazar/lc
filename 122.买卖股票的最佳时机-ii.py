#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

from typing import List

# @lc code=start
# 我靠，所有的上坡都买入
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index1, index2 = 0, 0
        curprofit = 0
        profit = 0
        for index in range(1, len(prices)):
            if(prices[index]>prices[index-1]):
                index2 = index
                curprofit = prices[index2] - prices[index1]
            else:
                profit = profit + curprofit
                curprofit = 0
                index1 = index
                index2 = index
        
        profit = profit + curprofit
        return profit
# @lc code=end

if __name__ == "__main__":
    a = Solution().maxProfit([7,1,5,3,6,4])
    print(a)
