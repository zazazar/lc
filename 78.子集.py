#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List

# @lc code=start
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []  # 结果
#         path = []  
#         def backtrack(nums,startIndex):
#             res.append(path[:])  #收集子集，要放在终止添加的上面，否则会漏掉自己
#             for i in range(startIndex,len(nums)):  #当startIndex已经大于数组的长度了，就终止了，for循环本来也结束了，所以不需要终止条件
#                 path.append(nums[i])
#                 backtrack(nums,i+1)  #递归
#                 path.pop()  #回溯
#         backtrack(nums,0)
#         print(res)
#         return res

# 回溯法   
# 1.加此轮的数据加入 list。
# 2.递归进行下一步调用。
# 3.删除此轮加入的数据进行回溯。

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # result
        path = []
        # []一定是子集之一
        res.append(path[:])

        def backtrack(nums, startIndex):
            # 先定义终止条件 没有返回
            if(startIndex >= len(nums)):
                return

            # path就是当前路径，每个路径都加入res
            # [0,1,2] [1,2] 每次递归的i都不同
            for i in range(startIndex, len(nums)):                
                path.append(nums[i])
                res.append(path[:])
                backtrack(nums, i+1)
                path.pop()
        
        backtrack(nums,0)
        return res


# @lc code=end
if __name__ == "__main__":
    Solution().subsets([1,2,3])

    for i in range(2,3):
        print(i)
