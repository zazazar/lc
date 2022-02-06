#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

from typing import List

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        dp = [[0 for i in range(len1+1)] for j in range(len2+1)]
        sol = 0
        

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if nums1[i-1]==nums2[j-1]:
                        dp[j][i] = dp[j-1][i-1]+1
                sol = max(sol,dp[j][i])

        return sol
                        

# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    sol.findLength([2,3,2,1],[3,4,3,2,1])

