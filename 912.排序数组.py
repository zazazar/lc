#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
from typing import List
import math

# @lc code=start
class Solution:
    # 快排
    def quicksortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def quick(left, right):
            if left >= right:
                return nums
            pivot = left
            i = left
            j = right

            while i < j:
                while i < j and nums[pivot] < nums[j]:
                    j = j - 1
                while i < j and nums[pivot] >= nums[i]:
                    i = i + 1
                a = nums[i]
                nums[i] = nums[j]
                nums[j] = a
            # i == j
            b = nums[pivot]
            nums[pivot] = nums[i]
            nums[i] = b

            quick(left, i - 1)
            quick(i + 1, right)

            return nums

        return quick(0, n - 1)

    # 归并
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        leftarr = self.sortArray(nums[:len(nums)//2])
        rightarr = self.sortArray(nums[len(nums)//2:])
        return self.merge(leftarr,rightarr)

    def merge(self,left_arr, right_arr):
        i, j = 0, 0
        newarr = []
        while i <= len(left_arr) - 1 and j <= len(right_arr) - 1:
            if left_arr[i] < right_arr[j]:
                newarr.append(left_arr[i])
                i = i + 1
            elif left_arr[i] == right_arr[j]:
                newarr.append(left_arr[i])
                newarr.append(right_arr[j])
                i += 1
                j += 1
            else:
                newarr.append(right_arr[j])
                j += 1
            
            if i == len(left_arr):
                # newarr.append(left_arr[i])
                newarr = newarr + right_arr[j:]
                break
            if j == len(right_arr):
                # newarr.append(right_arr[j])
                newarr = newarr + left_arr[i:]
                break
        return newarr



# @lc code=end
if __name__ == "__main__":
    sol = Solution().sortArray([9, 2, 3, 1, 4, 7, 6, 10])
    print(sol)




