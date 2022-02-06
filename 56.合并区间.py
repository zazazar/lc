#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        finalarr = []
        finalarr.append(intervals[0])
        
        for index,x in enumerate(intervals):
            last = finalarr[-1]
            if x[0]>last[1]:
                finalarr.append(x)
            else:
                if x[1]<=last[1]:
                    pass
                else:
                    finalarr.pop()
                    finalarr.append([last[0], x[1]])
        
        return finalarr

# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    sol.merge([[1,3],[2,6],[8,10],[15,18]])
