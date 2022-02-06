#!/usr/bin/env python
# coding:utf-8
class Solution:

    def maxSubArray(self, nums) -> int:
        """

        :param nums:
        :return:
        """
        sum = 0
        ans = nums[0]
        cur = [nums[0]]
        res = []

        for index, num in enumerate(nums):

            if sum <= 0:
                sum = num
                ans = max(sum, ans)

                if sum == ans:
                    cur = [num]
                    print(cur)

            else:
                sum = sum + num
                ans = max(sum, ans)
                cur.append(num)
                print(cur)
                if ans == sum:
                    res[:] = cur[:]

        return ans, res

    # 输出最大和对应的数组，，迷思


if __name__ == '__main__':
    sol = Solution()
    # sol.maxSubArray([-2, 1, -3, 4, -1, 2, 2, -8, 6, -3])
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -10, 100]))
