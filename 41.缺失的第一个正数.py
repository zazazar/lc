#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
from typing import List

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        indexarr = [0 for i in range(len(nums))]
        ans = -1

        for i in range(len(nums)) :
            if (nums[i]>=1 and nums[i]<=len(nums)):
                indexarr[nums[i]-1] = -1
        for j in range(len(nums)):
            if(indexarr[j]==0):
                ans = j+1
                break

        if ans == -1:
            ans = len(nums)+1
        
        return ans
            
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    sol.firstMissingPositive([1])

