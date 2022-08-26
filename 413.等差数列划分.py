#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
from ast import List
from operator import le


class Solution:
    def numberOfArithmeticSlices(self, nums):
        if(len(nums)<3):
            return 0
        n = len(nums)
        l = r = ans = 0
        
        while l < n-2 :
            d = nums[l+1] - nums[l]
            while r < n-1 and nums[r+1]-nums[r] == d:
                r += 1
            ans += (r-l) *(r-l-1)//2
            l = r
        return ans
            
                
        
                
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    sol.numberOfArithmeticSlices([1, 2, 4, 5, 7, 9])