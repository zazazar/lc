#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start

class Solution:
    def totalMoney(self, n: int) -> int:
        z = n % 7
        y = n//7
        sumy, sumz = 0,0
        
        if y>=1:
            sumy = y*(7*y+49)/2

        sumz = (2*y + 1 + z) * z / 2

        return int(sumy+sumz)


# @lc code=end

print(4//7)