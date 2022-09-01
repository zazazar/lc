#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start


class Solution:

    def permute(self, nums):

        def dfs(nums, path, used, res, depth):
            if depth == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):

                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    dfs(nums, path, used, res, depth + 1)
                    path.pop()
                    used[i] = False

            return res

        if not nums:
            return []

        path = []
        used = [False for _ in range(len(nums))]
        res = []
        return dfs(nums, path, used, res, 0)


# @lc code=end

if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
