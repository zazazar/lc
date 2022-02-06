#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index, num in enumerate(nums):
            dic[num] = index

        for index, num in enumerate(nums):
            otherindex = dic.get(target - num)
            if otherindex != index and otherindex is not None:
                return [index, otherindex]


# @lc code=end

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 3, 4, 5, 6], 9))
