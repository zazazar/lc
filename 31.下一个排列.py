#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from typing import List

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        index = -1
        for i in range(length-1,-1,-1):
            if nums[i-1]<nums[i] :
                index = i-1
                break

        for j in range(length-1,-1,-1):
            if nums[j]>nums[index]:
                middle = nums[j]
                nums[j] = nums[index]
                nums[index] = middle
                break
        
        restarr = nums[index+1:]
        restarr.sort()
        nums[index+1:] = restarr[:] 
        print(nums)

# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    sol.nextPermutation([4,3,2,1])
