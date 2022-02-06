#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

#         # if nums.__contains__(target)==False:
#         #     return -1
#         # else:
#         #     return nums.index(target)

#         # if target in nums:
#         #     return nums.index(target)
#         # else:
#         #     return -1

#         return nums.index(target) if target in nums else -1


class Solution:
    def bisearch(self, nums, startindex, target):
        start = 0
        end = len(nums)-1
        mid = int((start+end)/2)

        while(nums[mid] != target):
            if nums[mid] > target:
                end = mid-1
                mid = int((start+end)/2)
            else:
                start = mid+1
                mid = int((start+end)/2)
        return mid+startindex

    def search(self, nums: List[int], target: int) -> int:
        if nums.__contains__(target)==False:
            return -1
        
        start = 0
        end = len(nums)-1
        mid = int((start+end)/2)
        
        if target == nums[mid]:
            return mid
        
        while target != nums[mid]:
            if nums[start] < nums[mid]:  # 左边是有序的
                if target <= nums[mid] and target>=nums[start]:
                    tararr = nums[start:mid+1]
                    return self.bisearch(tararr, start, target)
                else:
                    start = mid+1
                    mid = int((start+end)/2)
            else:
                if target >= nums[mid+1] and target<=nums[end]:
                    # 这里也可以应用start和end直接在本区间二分！！！！
                    # 想多了！！！！
                    tararr = nums[mid+1:end+1]
                    return self.bisearch(tararr, mid+1, target)
                else:
                    end = mid
                    mid = int((start+end)/2)

            if target == nums[mid]:
                return mid

                # @lc code=end
if __name__ == '__main__':
    sol = Solution()
    # print(sol.search([1, 5, 6, 7, 0, 1, 2],0))
    print(sol.search([1, 3],3))

