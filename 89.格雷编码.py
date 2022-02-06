#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) :
        res = [0]
        head = 1

        for i in range(n):
            for j in range(len(res)-1, -1, -1):
                res.append(res[j]+head)
            head <<= 1

        return res

# @lc code=end
if __name__=="__main__":
    Solution().grayCode(3)

