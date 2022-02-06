# class Solution:
#     def maxProfit(self, prices) -> int:
#         maxprofit = 0
#         curprofit = 0
#         for index, num in enumerate(prices):
#             for i in range(index + 1, len(prices)):
#                 if (prices[i] > prices[index]):
#                     curprofit = prices[i] - prices[index]
#                     maxprofit = max(maxprofit, curprofit)
#         return maxprofit

class Solution:
    def maxProfit(self, prices) -> int:
        minPrice = 1e9
        profit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            profit = max(profit, price-minPrice)
        return profit


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
