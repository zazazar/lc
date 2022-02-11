#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = self.preSum(nums)  

    def preSum(selef,nums):
        presum = [0]
        for item in nums:
            presum.append(presum[-1]+item)
        return presum

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1] - self.presum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

