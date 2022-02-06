#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

from typing import List

# @lc code=start
# 这样是不对滴——
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         index1, index2 = 0, 0
#         curprofit = 0
#         profit = [0]
#         for index in range(1, len(prices)):
#             if(prices[index]>prices[index-1]):
#                 index2 = index
#                 curprofit = prices[index2] - prices[index1]
#             else:
#                 profit.append(curprofit)
#                 curprofit = 0
#                 index1 = index
#                 index2 = index
        
#         profit.append(curprofit)
#         profit.sort(reverse=True)

#         if(len(profit)>1):
#             return profit[0]+profit[1]
#         else:
#             return profit[0]


# @lc code=end

if __name__ == "__main__":
    a = Solution().maxProfit([3,3,5,0,0,3,1,4])
    print(a)
